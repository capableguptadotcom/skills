"""Turn an everystate -json result into a Mermaid statechart and a numbered bug path, in the reader's words.

Usage:
    python trace_chart.py RESULT.json [--labels LABELS.json] [--dot GRAPH.dot] [--max-states 30]

RESULT.json is the last line everystate prints with -json. LABELS.json (optional) names states, steps and rules:

    {"states": [{"when": {"phase": "paid"}, "label": "Paid"}],   first match wins; a value may be a list
     "show": ["phase", "charges"],                                variables in a state's default label
     "actions": {"Charge": "the server charges the card"},
     "rules": {"ChargedOnce": "a customer is charged at most once"}}

GRAPH.dot (optional) is everystate's `-dump dot,actionlabels` output; with it, a small model is drawn whole
and the bug path is marked on it. Reads files and prints to stdout; writes nothing and uses no network.
"""
import argparse
import json
import re
import sys
from pathlib import Path

BROKEN = {'invariant': 'breaks', 'invariant-init': 'breaks in the first state', 'deadlock': 'gets stuck',
          'liveness': 'never happens', 'error': 'stops on an error'}


def plain(value):
    """A TLA+ value as text: strings lose their quotes."""
    value = str(value).strip()
    return value[1:-1] if len(value) >= 2 and value[0] == value[-1] == '"' else value


def state_label(state, labels):
    for rule in labels.get('states', []):
        wanted = rule.get('when', {})
        if all(plain(state.get(k, '')) in ([str(v) for v in w] if isinstance(w, list) else [str(w)])
               for k, w in wanted.items()):
            return rule['label']
    shown = labels.get('show') or sorted(state)
    return ', '.join(f'{k} = {plain(state[k])}' for k in shown if k in state)


def step_label(action, labels):
    return labels.get('actions', {}).get(action, action or 'start')


def mermaid_text(text):
    return re.sub(r'\s+', ' ', str(text)).replace('"', "'").replace(';', ',').strip()


def dot_graph(path):
    """States (id -> variables) and edges (from, action, to) of a -dump dot,actionlabels file."""
    states, edges = {}, []
    for line in Path(path).read_text(encoding='utf-8', errors='replace').splitlines():
        if m := re.match(r'^(-?\d+) -> (-?\d+) \[label="((?:[^"\\]|\\.)*)"', line):
            edges.append((m[1], m[3], m[2]))
        elif m := re.match(r'^(-?\d+) \[label="((?:[^"\\]|\\.)*)"', line):
            text = m[2].replace('\\"', '"').replace('\\\\', '\\')
            variables = {}
            for part in text.split('\\n'):
                part = part.strip()
                part = part[2:].strip() if part.startswith('/\\') else part
                if ' = ' in part:
                    name, value = part.split(' = ', 1)
                    variables[name.strip()] = value.strip()
            states[m[1]] = variables
    return states, edges


def chart(result, labels, dot=None, max_states=30):
    trace = result.get('trace') or []
    names = {}  # label -> mermaid id

    def node(label):
        return names.setdefault(label, f's{len(names)}')

    path_labels = [state_label(step['state'], labels) for step in trace]
    lines, edges = ['stateDiagram-v2', '  direction LR'], []
    whole = False
    if dot:
        states, dot_edges = dot_graph(dot)
        drawn = {sid: state_label(v, labels) for sid, v in states.items()}
        if len(set(drawn.values())) <= max_states:
            whole = True
            seen = set()
            for a, action, b in dot_edges:
                key = (drawn.get(a), step_label(action, labels), drawn.get(b))
                if None in key or key[0] == key[2] or key in seen:
                    continue
                seen.add(key)
                edges.append(f'  {node(key[0])} --> {node(key[2])}: {mermaid_text(key[1])}')
            first = [drawn[s] for s in states][:1]
            starts = first or path_labels[:1]
        else:
            starts = path_labels[:1]
    else:
        starts = path_labels[:1]
    if not whole:
        for i in range(1, len(trace)):
            edges.append(f'  {node(path_labels[i - 1])} --> {node(path_labels[i])}: '
                         f'{i}. {mermaid_text(step_label(trace[i].get("action"), labels))}')
        if result.get('status') == 'liveness' and result.get('loopTo') is not None and trace:
            edges.append(f'  {node(path_labels[-1])} --> {node(path_labels[result["loopTo"]])}: '
                         f'{mermaid_text("and again, forever")}')
    for label in starts:
        edges.insert(0, f'  [*] --> {node(label)}')
    for label, sid in names.items():
        lines.append(f'  state "{mermaid_text(label)}" as {sid}')
    lines += edges
    if trace and result.get('status') in BROKEN:
        lines.append('  classDef breaks fill:#fde2e2,stroke:#b42318,color:#7a271a')
        lines.append(f'  class {node(path_labels[-1])} breaks')
        if whole:
            on_path = sorted({node(l) for l in path_labels[:-1]} - {node(path_labels[-1])})
            if on_path:
                lines.append('  classDef path stroke:#b42318,stroke-width:2px')
                lines.append(f'  class {",".join(on_path)} path')
    return '\n'.join(lines)


def story(result, labels):
    status, name = result.get('status'), result.get('name')
    count = result.get('distinct')
    if status == 'ok':
        return f'No rule breaks: everystate checked every reachable state ({count} distinct) at these bounds.'
    rule = labels.get('rules', {}).get(name, name) if name else None
    head = f'{name or "The model"} {BROKEN.get(status, status)}'
    head += f' ({rule}).' if rule and rule != name else '.'
    if status == 'error' and result.get('message'):
        head += f' everystate says: {result["message"].splitlines()[0]}'
    trace = result.get('trace') or []
    lines = [head, f'Shortest path, {max(len(trace) - 1, 0)} steps:'] if trace else [head]
    for i, step in enumerate(trace):
        label = state_label(step['state'], labels)
        lines.append(f'{i}. {label}' if i == 0 else f'{i}. {step_label(step.get("action"), labels)}: {label}')
    if status == 'liveness' and result.get('loopTo') is not None:
        lines.append(f'Then it goes back to step {result["loopTo"]} and repeats forever.')
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('result')
    parser.add_argument('--labels')
    parser.add_argument('--dot')
    parser.add_argument('--max-states', type=int, default=30)
    args = parser.parse_args()
    lines = [l for l in Path(args.result).read_text(encoding='utf-8-sig').splitlines() if l.strip().startswith('{')]
    if not lines:
        sys.exit(f'{args.result} holds no everystate -json result.')
    result = json.loads(lines[-1])
    labels = json.loads(Path(args.labels).read_text(encoding='utf-8')) if args.labels else {}
    print('```mermaid\n' + chart(result, labels, args.dot, args.max_states) + '\n```\n')
    print(story(result, labels))
    return 0


if __name__ == '__main__':
    sys.exit(main())

from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from validate import ROOT, frontmatter, validate

EXPLICIT_YAML = 'policy:\n  allow_implicit_invocation: false\n'


class SkillFixture:
    def __init__(self, root):
        self.root = Path(root)

    def skill(self, name='fixture', body='', frontmatter=None, files=None):
        folder = self.root / 'skills' / name
        folder.mkdir(parents=True)
        meta = frontmatter or f'name: {name}\ndescription: A fixture'
        (folder / 'SKILL.md').write_text(f'---\n{meta}\n---\n{body}\n', encoding='utf-8')
        for relative, content in (files or {}).items():
            path = folder / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding='utf-8')
        return folder

    def errors(self):
        return validate(self.root)[0]


class RealSkillTests(unittest.TestCase):
    def test_each_real_skill_installs_alone(self):
        for source in (ROOT / 'skills').iterdir():
            if not source.is_dir():
                continue
            with self.subTest(skill=source.name), tempfile.TemporaryDirectory() as tmp:
                shutil.copytree(source, Path(tmp) / 'skills' / source.name,
                                ignore=shutil.ignore_patterns('__pycache__'))
                errors, names = validate(Path(tmp))
                self.assertEqual(errors, [])
                self.assertEqual(names, [source.name])

    def test_explicit_skills_are_explicit_in_both_hosts(self):
        expected = {'handoff', 'simulate-discussion', 'skill-feedback'}
        for name in expected:
            text = (ROOT / 'skills' / name / 'SKILL.md').read_text(encoding='utf-8')
            self.assertIn('disable-model-invocation: true', text, name)
            config = (ROOT / 'skills' / name / 'agents' / 'openai.yaml').read_text(encoding='utf-8')
            self.assertIn('allow_implicit_invocation: false', config, name)

    def test_skill_feedback_posts_only_where_the_user_can_push(self):
        """People using the pack do private work. The feedback skill never chooses where to post (such as the
        pack's own public repository), posts only where the signed-in account can push, and never forks. So
        a maintainer's scheduled run can open PRs on the pack, and a team member's run cannot."""
        text = (ROOT / 'skills' / 'skill-feedback' / 'SKILL.md').read_text(encoding='utf-8')
        self.assertNotRegex(text, r'Otherwise use the skill.s `source` repository')
        self.assertIn('Never pick one yourself', text)
        self.assertIn('--jq .permissions.push', text)
        self.assertIn('Never fork', text)
        self.assertIn('scheduled run that the user set up, with the repository named in its prompt', text)
        self.assertNotRegex(text.lower(), r"host's scheduler|\bcron\b")

    def test_skill_feedback_is_left_out_of_a_plain_install(self):
        """The skills CLI skips skills marked internal unless INSTALL_INTERNAL_SKILLS=1, so a team's
        `npx skills add <repo>` gets the daily skills without the maintainers' feedback tool."""
        for source in (ROOT / 'skills').iterdir():
            if not source.is_dir():
                continue
            meta = frontmatter((source / 'SKILL.md').read_text(encoding='utf-8'))
            internal = (meta.get('metadata') or {}).get('internal', False)
            self.assertIs(internal, source.name == 'skill-feedback', source.name)


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.fx = SkillFixture(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def assertError(self, fragment):
        errors = self.fx.errors()
        self.assertTrue(any(fragment in e for e in errors), errors)

    def test_clean_fixture_passes(self):
        self.fx.skill()
        self.assertEqual(self.fx.errors(), [])

    def test_missing_reference_is_reported(self):
        self.fx.skill(body='[testing](references/testing.md)')
        self.assertError('missing reference')

    def test_sibling_reference_is_rejected_even_when_present(self):
        self.fx.skill(body='[peer](../peer/SKILL.md)')
        self.fx.skill(name='peer')
        self.assertError('leaves the skill folder')

    def test_nested_references_are_checked(self):
        self.fx.skill(body='[guide](references/guide.md)',
                      files={'references/guide.md': '[details](missing.md)\n'})
        self.assertError('missing.md')

    def test_malformed_frontmatter_fails(self):
        self.fx.skill(frontmatter='name: fixture\ndescription: unquoted: value')
        self.assertTrue(self.fx.errors())

    def test_name_rules(self):
        cases = {'Fixture': 'lowercase', 'fix--ture': 'lowercase', 'review': 'collides'}
        for name, fragment in cases.items():
            with self.subTest(name=name), tempfile.TemporaryDirectory() as tmp:
                fx = SkillFixture(tmp)
                fx.skill(name=name)
                self.assertTrue(any(fragment in e for e in fx.errors()), fx.errors())

    def test_name_must_match_folder(self):
        self.fx.skill(frontmatter='name: other\ndescription: A fixture')
        self.assertError('must match its folder')

    def test_long_description_fails(self):
        self.fx.skill(frontmatter='name: fixture\ndescription: ' + 'word ' * 90)
        self.assertError('keep it under')

    def test_unknown_frontmatter_key_fails(self):
        self.fx.skill(frontmatter='name: fixture\ndescription: A fixture\nmodel: fast')
        self.assertError('unsupported frontmatter keys: model')

    def test_long_body_fails(self):
        self.fx.skill(body='line\n' * 501)
        self.assertError('over 500 lines')

    def test_explicit_needs_both_settings(self):
        self.fx.skill(frontmatter='name: fixture\ndescription: A fixture\ndisable-model-invocation: true')
        self.assertError('not in Codex')

    def test_codex_explicit_needs_claude_setting(self):
        self.fx.skill(files={'agents/openai.yaml': EXPLICIT_YAML})
        self.assertError('not in Claude Code')

    def test_matching_explicit_settings_pass(self):
        self.fx.skill(frontmatter='name: fixture\ndescription: A fixture\ndisable-model-invocation: true',
                      files={'agents/openai.yaml': EXPLICIT_YAML})
        self.assertEqual(self.fx.errors(), [])

    def test_tool_server_config_is_rejected(self):
        self.fx.skill(files={'.mcp.json': '{}'})
        self.assertError('tool servers')

    def test_non_python_script_is_rejected(self):
        self.fx.skill(files={'scripts/run.sh': 'echo hi\n'})
        self.assertError('must be Python')

    def test_network_script_is_rejected(self):
        self.fx.skill(files={'scripts/fetch.py': 'import urllib.request\n'})
        self.assertError('must not use the network')

    def test_personal_path_is_rejected(self):
        self.fx.skill(body='See C:\\Users\\someone\\notes.md')
        self.assertError('personal path')


if __name__ == '__main__':
    unittest.main()

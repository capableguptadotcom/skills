from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from validate import ROOT, validate


class StandaloneSkillTests(unittest.TestCase):
    def test_each_real_skill_survives_installation_without_its_peers(self):
        for source in (ROOT / 'skills').iterdir():
            if not source.is_dir():
                continue
            with self.subTest(skill=source.name), tempfile.TemporaryDirectory() as tmp:
                target = Path(tmp)
                shutil.copytree(source, target / 'skills' / source.name)
                errors, names = validate(target)
                self.assertEqual(errors, [])
                self.assertEqual(names, [source.name])

    def fixture(self, target, body='', frontmatter=None):
        skill = target / 'skills' / 'kp-fixture'
        skill.mkdir(parents=True)
        meta = frontmatter or 'name: kp-fixture\ndescription: A fixture'
        (skill / 'SKILL.md').write_text(f'---\n{meta}\n---\n{body}\n', encoding='utf-8')
        return skill

    def test_missing_conditional_reference_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            self.fixture(target, '[testing](references/testing.md)')
            errors, _ = validate(target)
            self.assertTrue(any('missing reference' in e for e in errors))

    def test_a_sibling_dependency_is_rejected_even_when_present(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            self.fixture(target, '[peer](../kp-peer/SKILL.md)')
            peer = target / 'skills' / 'kp-peer'
            peer.mkdir()
            (peer / 'SKILL.md').write_text('---\nname: kp-peer\ndescription: A peer\n---\n', encoding='utf-8')
            errors, _ = validate(target)
            self.assertTrue(any('reference leaves' in e for e in errors))

    def test_nested_references_are_checked(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            skill = self.fixture(target, '[guide](references/guide.md)')
            (skill / 'references').mkdir()
            (skill / 'references/guide.md').write_text('[details](missing.md)\n', encoding='utf-8')
            errors, _ = validate(target)
            self.assertTrue(any('missing.md' in e for e in errors))

    def test_malformed_frontmatter_fails_validation(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            self.fixture(target, frontmatter='name: kp-fixture\ndescription: unquoted: value')
            errors, _ = validate(target)
            self.assertTrue(errors)


if __name__ == '__main__':
    unittest.main()

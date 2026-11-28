import unittest

from tags import normalize_tags, tag_line


class TagTests(unittest.TestCase):
    def test_dedupes_and_keeps_order(self):
        self.assertEqual(normalize_tags("Python, web,python , API"), ["python", "web", "api"])

    def test_empty_parts_are_dropped(self):
        self.assertEqual(normalize_tags(" , ,go"), ["go"])

    def test_tag_line_single(self):
        self.assertEqual(tag_line("Rust"), "#rust")


if __name__ == "__main__":
    unittest.main()

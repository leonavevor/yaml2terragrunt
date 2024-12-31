import unittest

from src.config_parser import parse_config


class TestConfigParser(unittest.TestCase):
    def test_parse_config(self):
        config = parse_config("tests/test.yaml")
        self.assertIn("parameters", config)
        self.assertIn("modules", config)


if __name__ == "__main__":
    unittest.main()

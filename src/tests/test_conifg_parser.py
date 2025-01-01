import unittest

from src.config_parser import parse_config


class TestConfigParser(unittest.TestCase):
    def test_parse_config(self):
        config = parse_config("./src/tests/sample_tg_declaration.yaml")
        self.assertIn("parameters", config)
        self.assertIn("modules", config)


if __name__ == "__main__":
    unittest.main()

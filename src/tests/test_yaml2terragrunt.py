import os
import unittest
import yaml
from yaml2terragrunt import load_yaml, create_directory_structure, create_terragrunt_hcl, main

class TestYaml2Terragrunt(unittest.TestCase):

    def setUp(self):
        self.yaml_file = './src/tests/sample_tg_declaration.yaml'
        self.config = load_yaml(self.yaml_file)
        self.base_path = os.path.dirname(self.yaml_file)

    def test_load_yaml(self):
        config = load_yaml(self.yaml_file)
        self.assertIsInstance(config, dict)
        self.assertIn('parameters', config)
        self.assertIn('globals', config)
        self.assertIn('modules', config)

    def test_create_directory_structure(self):
        create_directory_structure(self.base_path, self.config['modules'])
        for module in self.config['modules']:
            module_path = os.path.join(self.base_path, module['name'])
            self.assertTrue(os.path.exists(module_path))
            self.assertTrue(os.path.isdir(module_path))

    def test_create_terragrunt_hcl(self):
        for module in self.config['modules']:
            context = {
                'module': module,
                'param': self.config['parameters'],
                'var': self.config['globals']['vars'],
                'environment': self.config['globals']['environment']
            }
            hcl_content = create_terragrunt_hcl(module, context)
            self.assertIn('terraform', hcl_content)
            self.assertIn('inputs', hcl_content)
            self.assertIn('outputs', hcl_content)
            if 'depends_on' in module:
                self.assertIn('dependencies', hcl_content)
            if 'dependencies' in module:
                self.assertIn('dependency', hcl_content)
            if 'hooks' in module:
                self.assertIn('hooks', hcl_content)
            if 'retries' in module:
                self.assertIn('retry', hcl_content)

    def test_main(self):
        main(self.yaml_file)
        for module in self.config['modules']:
            hcl_file_path = os.path.join(self.base_path, module['name'], 'terragrunt.hcl')
            self.assertTrue(os.path.exists(hcl_file_path))
            with open(hcl_file_path, 'r') as hcl_file:
                hcl_content = hcl_file.read()
                self.assertIn('terraform', hcl_content)
                self.assertIn('inputs', hcl_content)
                self.assertIn('outputs', hcl_content)
                if 'depends_on' in module:
                    self.assertIn('dependencies', hcl_content)
                if 'dependencies' in module:
                    self.assertIn('dependency', hcl_content)
                if 'hooks' in module:
                    self.assertIn('hooks', hcl_content)
                if 'retries' in module:
                    self.assertIn('retry', hcl_content)

if __name__ == '__main__':
    unittest.main()

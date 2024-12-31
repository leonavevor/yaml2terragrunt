import os

from src.terragrunt_executor import execute_terragrunt


def generate_terragrunt_files(config):
    # Create the root terragrunt.hcl file
    root_path = "./terragrunt/"
    os.makedirs(root_path, exist_ok=True)

    # Create the root terragrunt.hcl file
    with open(os.path.join(root_path, "terragrunt.hcl"), "w") as root_file:
        root_file.write("# Root Terragrunt configuration\n")
        # root_file.write("terraform {\n  source = \"./modules\"\n}\n")

    # Create terragrunt child directories (modules) and files based on the config
    for module in config["modules"]:
        module_path = os.path.join(root_path, module["name"])
        os.makedirs(module_path, exist_ok=True)

        with open(os.path.join(module_path, "terragrunt.hcl"), "w") as file:
            file.write(f"# Terragrunt configuration for {module['name']}\n")
            file.write(f"locals {{\n  # Add locals here\n}}\n")
            file.write(f'include "root" {{\n  path = find_in_parent_folders()\n}}\n')
            #file.write(f"dependency \"{module['depends_on']}\" {{\n # Add dependencies here\n}}\n")
            if "git::" in module["source"]:
                file.write(f"terraform {{\n  source = \"{module['source']}\"\n # Add additional configuration here\n}}\n")
            else:
                file.write(f"terraform {{\n  source = \"${{get_repo_root()}}/{module['source']}\"\n  # Add additional configuration here\n}}\n")
            file.write(f"inputs = {{\n # Add inputs here\n}}\n")

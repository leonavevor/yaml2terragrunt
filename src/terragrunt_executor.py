import os
import subprocess


def execute_terragrunt(config: dict = {}, root_path: str = "./terragrunt/", action: str = "plan", fail_fast: bool = False, **kwargs):
    for module in config["modules"]:
        # module_path = os.path.join(root_path, module["name"])
        tg_args: list = []
        for key, value in kwargs.items():
            tg_args.append(f"{key}={value} ")
        subprocess.run(
            ["terragrunt", action] + tg_args,
            cwd=root_path,
            check=fail_fast,
        )


# get parent dire of modulepath

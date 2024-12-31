import os
import subprocess


def execute_terragrunt(
    config: dict = {},  # TODO: make use of converted yaml declaration to dict
    root_path: str = "./terragrunt/",
    action: str = "plan",
    fail_fast: bool = False,
    **kwargs,
):
    tg_kwargs: list = []
    sub_path: str = ""
    for _, value in kwargs.items():
        for k, v in value.items():
            tg_kwargs.append(f"{k}={v} ")
            if "--terragrunt-working-dir" not in k:
                sub_path = os.path.join(root_path, v)
    subprocess.run(
        ["terragrunt", "run-all", action, *tg_kwargs],
        shell=False,
        cwd=sub_path or root_path,
        check=fail_fast,
    )

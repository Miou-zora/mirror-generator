#!/usr/bin/env python3
##
## @VyOkPROJECT, 2023
## mirror-generator
## File description:
## why do you look at this aweful code ...
##

import subprocess

def push_mirror(mirror_name: str, binary_name: str):
    actions = [(["git", "-C", f"{binary_name}/{mirror_name}/", "add", "."], "No add can be done"),
               (["git", "-C", f"{binary_name}/{mirror_name}/", "commit", "-m", "CI/CD push"], "No commit can be done"),
               (["git", "-C", f"{binary_name}/{mirror_name}/", "push"], "No push can be done")]
    for action in actions:
        if subprocess.run(action[0]).returncode == 1:
            print(action[1])
            exit(84)

import subprocess


def execute(command):

    result = subprocess.run(
        command,
        shell=True,
        executable="/bin/bash",
        capture_output=True,
        text=True
    )

    return result.stdout.splitlines()
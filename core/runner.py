import subprocess


def run(command):
    """
    Execute a shell command and return its output as a list of lines.
    """

    result = subprocess.run(
        command,
        shell=True,
        executable="/bin/bash",
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return []

    return result.stdout.splitlines()
import subprocess

def execute(urls):
    process = subprocess.run(
        ["uro"],
        input="\n".join(urls),
        text=True,
        capture_output=True
    )
    return process.stdout.splitlines()
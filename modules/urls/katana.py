from core.runner import run

def execute(urls):
    return run("echo '{}' | /home/kali/tools/go/bin/katana -silent".format("\n".join(urls)))
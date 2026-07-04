from core.runner import run

def execute(urls):
    return run("echo '{}' |katana -silent".format("\n".join(urls)))
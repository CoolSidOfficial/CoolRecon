from core.runner import run


def execute(domains):

    hosts = "\n".join(domains)


    command = (
        f"echo '{hosts}' | "
        f"httpx -silent"
    )


    return run(command)
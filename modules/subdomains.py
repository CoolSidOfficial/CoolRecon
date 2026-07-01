from core.runner import run


def execute(domain):

    command = (
        f"subfinder "
        f"-d {domain} "
        f"-silent"
    )


    results = run(command)


    return list(
        set(results)
    )
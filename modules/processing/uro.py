from core.runner import run


def execute(urls):
    """
    Clean URLs using uro (removes noise, duplicates, junk params)
    """

    input_data = "\n".join(urls)

    command = f"echo '{input_data}' | uro"

    results = run(command)

    return list(set(results))
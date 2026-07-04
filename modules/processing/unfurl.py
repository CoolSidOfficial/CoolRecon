from core.runner import run


def execute(urls):
    """
    Extract parameters, paths, domains from URLs
    """

    input_data = "\n".join(urls)

    command = f"echo '{input_data}' | unfurl --unique keys"

    return run(command)
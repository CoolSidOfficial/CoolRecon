from core.runner import run


def execute(urls):
    """
    XSS scanning using dalfox
    """

    input_data = "\n".join(urls)

    command = f"echo '{input_data}' | dalfox pipe"

    return run(command)
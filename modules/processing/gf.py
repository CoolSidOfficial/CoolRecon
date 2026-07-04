from core.runner import run


def execute(urls, pattern="xss"):
    """
    Filter URLs using gf patterns (xss, sqli, ssrf, etc.)
    """

    input_data = "\n".join(urls)

    command = f"echo '{input_data}' | gf {pattern}"

    return run(command)
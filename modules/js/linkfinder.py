from core.runner import run


def execute(urls):
    """
    Extract endpoints from JS files
    """

    input_data = "\n".join(urls)

    command = f"echo '{input_data}' | linkfinder -i {input_data} -o cli"

    return run(command)
from core.runner import run


def execute(hosts):
    """
    Fast port scanning using naabu
    """

    input_data = "\n".join(hosts)

    command = f"echo '{input_data}' | naabu -silent -top-ports 1000"

    return run(command)

from core.runner import run


def execute(subdomains):
    """
    Resolve subdomains using dnsx
    """

    input_data = "\n".join(subdomains)

    command = f"echo '{input_data}' | dnsx -silent"

    return run(command)

from core.runner import run


def execute(domain):
    """
    Extract JS files from domain
    """

    command = f"subjs -d {domain}"

    return run(command)
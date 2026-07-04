from core.runner import run


def execute(domain):
    """
    Run Subfinder to enumerate passive subdomains.

    Args:
        domain (str): Target domain.

    Returns:
        list: Discovered subdomains.
    """

    command = (
        f"subfinder "
        f"-d {domain} "
        f"-silent"
    )

    return run(command)
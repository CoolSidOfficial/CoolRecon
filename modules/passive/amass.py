
from core.runner import run


def execute(domain):
    """
    Run Amass passive enumeration for subdomains.

    Args:
        domain (str): Target domain

    Returns:
        list: Discovered subdomains
    """

    command = (
        f"amass enum "
        f"-passive "
        f"-d {domain}"
    )

    results = run(command)

    # Clean + deduplicate while preserving order
    seen = set()
    cleaned = []

    for sub in results:
        sub = sub.strip()

        if not sub:
            continue

        if sub in seen:
            continue

        seen.add(sub)
        cleaned.append(sub)

    return cleaned

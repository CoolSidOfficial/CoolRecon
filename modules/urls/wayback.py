
from core.runner import run


def execute(domain):
    """
    Fetch historical URLs using waybackurls.

    Args:
        domain (str): Target domain

    Returns:
        list: Archived URLs
    """

    command = f"waybackurls {domain}"

    results = run(command)

    # Clean output
    seen = set()
    cleaned = []

    for url in results:
        url = url.strip()

        if not url:
            continue

        if url in seen:
            continue

        seen.add(url)
        cleaned.append(url)

    return cleaned

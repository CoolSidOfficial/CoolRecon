from core.runner import run


def execute(domain):
    """
    Find subdomains from GitHub sources (github-subdomains tool)
    """

    command = f"github-subdomains -d {domain}"

    results = run(command)

    seen = set()
    cleaned = []

    for item in results:
        item = item.strip()

        if not item:
            continue

        if domain not in item:
            continue

        if item in seen:
            continue

        seen.add(item)
        cleaned.append(item)

    return cleaned
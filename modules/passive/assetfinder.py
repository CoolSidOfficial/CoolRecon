from core.runner import run


def execute(domain):
    """
    Passive subdomain enumeration using assetfinder
    """

    command = f"assetfinder --subs-only {domain}"

    results = run(command)

    seen = set()
    cleaned = []

    for item in results:
        item = item.strip()

        if not item:
            continue

        # keep only valid-looking subdomains
        if domain not in item:
            continue

        if item in seen:
            continue

        seen.add(item)
        cleaned.append(item)

    return cleaned
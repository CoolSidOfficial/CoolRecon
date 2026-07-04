from core.runner import run


def execute(domain):
    """
    Passive subdomain enumeration using Findomain.
    """

    command = (
        f"findomain "
        f"-t {domain} "
        f"-q"
    )

    results = run(command)

    seen = set()
    cleaned = []

    for item in results:
        item = item.strip().lower()

        if not item:
            continue

        if not item.endswith(domain):
            continue

        if item in seen:
            continue

        seen.add(item)
        cleaned.append(item)

    return cleaned
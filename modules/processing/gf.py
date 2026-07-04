from core.runner import run


def execute(urls, patterns=None):
    """
    Filter URLs using multiple gf patterns (xss, sqli, ssrf, redirect, etc.)
    Returns results grouped by pattern.
    """

    if not urls:
        return {}

    if patterns is None:
        patterns = ["xss"]

    # deduplicate input
    seen = set()
    cleaned = []

    for u in urls:
        u = u.strip()
        if not u:
            continue
        if u in seen:
            continue
        seen.add(u)
        cleaned.append(u)

    input_data = "\n".join(cleaned)

    results = {}

    for pattern in patterns:
        command = f"printf '%s\n' \"{input_data}\" | gf {pattern}"
        output = run(command)

        # clean + dedupe output per pattern
        seen_p = set()
        filtered = []

        for item in output:
            item = item.strip()
            if not item or item in seen_p:
                continue
            seen_p.add(item)
            filtered.append(item)

        results[pattern] = filtered

    return results
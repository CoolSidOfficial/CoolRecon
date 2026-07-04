def merge(*lists):
    seen = set()
    merged = []

    for lst in lists:
        for item in lst:
            item = item.strip()

            if not item:
                continue

            if item in seen:
                continue

            seen.add(item)
            merged.append(item)

    return merged
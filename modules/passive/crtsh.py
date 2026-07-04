import requests


def execute(domain):
    """
    Fetch subdomains from certificate transparency logs (crt.sh)
    """

    url = f"https://crt.sh/?q=%25.{domain}&output=json"

    try:
        response = requests.get(url, timeout=20)
        data = response.json()
    except:
        return []

    subs = set()

    for entry in data:
        name = entry.get("name_value", "")

        for sub in name.split("\n"):
            sub = sub.strip()

            if not sub:
                continue

            if domain in sub:
                subs.add(sub)

    return list(subs)
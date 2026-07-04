
import sys
from urllib.parse import urlparse

from core.logger import info
from core.storage import save
from core.merge import merge

from modules import subdomains
from modules.dns import dnsx
from modules import http_probe

from modules.urls import gau
from modules.urls import katana
from modules.urls import wayback


def normalize(target):
    if target.startswith("http://") or target.startswith("https://"):
        return urlparse(target).netloc
    return target


def extract_urls(live_hosts):
    """
    Extract clean URLs from httpx output
    """
    urls = []

    for line in live_hosts:
        parts = line.strip().split()

        if not parts:
            continue

        urls.append(parts[0])

    return urls


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <domain>")
        sys.exit(1)

    domain = normalize(sys.argv[1])

    info(f"CoolRecon started: {domain}")

    # 1. Subdomains
    subs = subdomains.execute(domain)
    info(f"Subdomains found: {len(subs)}")

    save(domain, "subdomains", "merged.txt", subs)

    # 2. DNS Resolve
    resolved = dnsx.execute(subs)
    info(f"Resolved: {len(resolved)}")

    save(domain, "dns", "resolved.txt", resolved)

    # 3. HTTP Probe
    live = http_probe.execute(resolved)
    info(f"Live hosts found: {len(live)}")

    save(domain, "http", "alive.txt", live)

    # Clean live URLs
    live_urls = extract_urls(live)

    # 4. GAU URLs
    gau_urls = gau.execute(domain)
    info(f"GAU URLs: {len(gau_urls)}")

    save(domain, "urls", "gau.txt", gau_urls)

    # 5. Katana crawl (FIXED INPUT)
    katana_urls = katana.execute(live_urls)
    info(f"Katana URLs: {len(katana_urls)}")

    save(domain, "urls", "katana.txt", katana_urls)

    # 6. Wayback URLs
    wayback_urls = wayback.execute(domain)
    info(f"Wayback URLs: {len(wayback_urls)}")

    save(domain, "urls", "wayback.txt", wayback_urls)

    # 7. Merge all URLs
    all_urls = merge(gau_urls, katana_urls, wayback_urls)

    save(domain, "urls", "merged.txt", all_urls)

    info("Completed")


if __name__ == "__main__":
    main()

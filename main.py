import sys
from urllib.parse import urlparse

from core.logger import info
from core.storage import save

from modules import subdomains
from modules import dnsx
from modules import http_probe
from modules.urls import gau
from modules import katana
from core.merge import merge


def normalize(target):
    if target.startswith("http://") or target.startswith("https://"):
        return urlparse(target).netloc
    return target


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

    # 4. URL Collection (GAU)
    gau_urls = gau.execute(domain)
    info(f"GAU URLs: {len(gau_urls)}")

    save(domain, "urls", "gau.txt", gau_urls)

    # 5. Crawling (Katana)
    katana_urls = katana.execute(live)
    info(f"Katana URLs: {len(katana_urls)}")

    save(domain, "urls", "katana.txt", katana_urls)

    # 6. Merge URLs
    urls = merge(gau_urls, katana_urls)
    save(domain, "urls", "merged.txt", urls)

    info("Completed")


if __name__ == "__main__":
    main()
```python id="main1"
import sys
from urllib.parse import urlparse

from core.logger import info
from core.storage import save
from core.merge import merge

# Subdomains
from modules import subdomains
from modules.passive import assetfinder, github, crtsh

# DNS
from modules.dns import dnsx

# HTTP
from modules import http_probe

# URLs
from modules.urls import gau, katana, wayback

# Processing
from modules.processing import uro, unfurl

# JS
from modules.js import subjs, linkfinder

# Ports
from modules.ports import naabu

# Vuln
from modules.vuln import nuclei, dalfox


def normalize(target):
    if target.startswith("http"):
        return urlparse(target).netloc
    return target


def extract_urls(live):
    urls = []
    for line in live:
        parts = line.split()
        if parts:
            urls.append(parts[0])
    return urls


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <domain>")
        sys.exit(1)

    domain = normalize(sys.argv[1])

    info(f"CoolRecon FULL PIPELINE STARTED: {domain}")

    # ----------------------------
    # 1. SUBDOMAIN ENUMERATION
    # ----------------------------
    subs = subdomains.execute(domain)
    subs += assetfinder.execute(domain)
    subs += github.execute(domain)
    subs += crtsh.execute(domain)

    subs = list(set(subs))
    info(f"Subdomains found: {len(subs)}")
    save(domain, "subdomains", "all.txt", subs)

    # ----------------------------
    # 2. DNS RESOLUTION
    # ----------------------------
    resolved = dnsx.execute(subs)
    info(f"Resolved: {len(resolved)}")
    save(domain, "dns", "resolved.txt", resolved)

    # ----------------------------
    # 3. HTTP PROBE
    # ----------------------------
    live = http_probe.execute(resolved)
    live_urls = extract_urls(live)

    info(f"Live hosts: {len(live_urls)}")
    save(domain, "http", "alive.txt", live)

    # ----------------------------
    # 4. URL COLLECTION
    # ----------------------------
    gau_urls = gau.execute(domain)
    katana_urls = katana.execute(live_urls)
    wayback_urls = wayback.execute(domain)

    urls = merge(gau_urls, katana_urls, wayback_urls)

    info(f"URLs collected: {len(urls)}")
    save(domain, "urls", "raw.txt", urls)

    # ----------------------------
    # 5. PROCESSING LAYER
    # ----------------------------
    clean_urls = uro.execute(urls)
    params = unfurl.execute(clean_urls)

    save(domain, "processing", "clean_urls.txt", clean_urls)
    save(domain, "processing", "params.txt", params)

    # ----------------------------
    # 6. JS EXTRACTION
    # ----------------------------
    js_files = subjs.execute(domain)
    js_endpoints = linkfinder.execute(js_files)

    save(domain, "js", "files.txt", js_files)
    save(domain, "js", "endpoints.txt", js_endpoints)

    # ----------------------------
    # 7. PORT SCANNING
    # ----------------------------
    ports = naabu.execute(live_urls)

    save(domain, "ports", "open_ports.txt", ports)

    # ----------------------------
    # 8. VULNERABILITY SCANNING
    # ----------------------------
    nuclei_results = nuclei.execute(live_urls)
    dalfox_results = dalfox.execute(urls)

    save(domain, "vuln", "nuclei.txt", nuclei_results)
    save(domain, "vuln", "xss.txt", dalfox_results)

    info("FULL PIPELINE COMPLETED")


if __name__ == "__main__":
    main()
```

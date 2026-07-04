import sys

from core.logger import info
from core.storage import save

from modules import subdomains
from modules import http_probe


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]

    info(f"CoolRecon started: {domain}")

    # Passive Subdomain Enumeration
    subs = subdomains.execute(domain)

    info(f"Subdomains found: {len(subs)}")

    save(
        domain,
        "subdomains",
        "merged.txt",
        subs
    )

    # HTTP Probe
    live = http_probe.execute(subs)

    info(f"Live hosts found: {len(live)}")

    save(
        domain,
        "http",
        "alive.txt",
        live
    )

    info("Completed")


if __name__ == "__main__":
    main()

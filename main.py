import sys

from core.logger import info
from core.storage import save

from modules import subdomains
from modules import http_probe



def main():

    domain = sys.argv[1]


    info(
        f"CoolRecon started: {domain}"
    )


    subs = subdomains.execute(domain)


    info(
        f"Subdomains found: {len(subs)}"
    )


    save(
        domain,
        "subdomains",
        subs
    )


    live = http_probe.execute(subs)


    info(
        f"Live hosts found: {len(live)}"
    )


    save(
        domain,
        "live_hosts",
        live
    )


    info(
        "Completed"
    )



if __name__ == "__main__":

    main()
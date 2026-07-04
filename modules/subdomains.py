from modules.passive import subfinder,amass
from core.merge import merge


def execute(domain):
    """
    Execute all passive subdomain enumeration modules.
    """

    subfinder_results = subfinder.execute(domain)

    amass_results = amass.execute(domain)
    # Future modules
    # github_results = github.execute(domain)
    # crtsh_results = crtsh.execute(domain)

    return merge(
        subfinder_results,
        amass_results,
        # github_results,
        # crtsh_results,
    )
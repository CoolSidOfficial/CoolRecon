from modules.passive import subfinder,amass,github,crtsh
from modules.passive import findomain,assetfinder
from core.merge import merge


def execute(domain):
    """
    Execute all passive subdomain enumeration modules.
    """

    subfinder_results = subfinder.execute(domain)

    amass_results = amass.execute(domain)
    github_results = github.execute(domain)
    crtsh_results = crtsh.execute(domain)
    findomain_results = findomain.execute(domain)
    assetfinder_results = assetfinder.execute(domain)



    return merge(
        subfinder_results,
        amass_results,
        github_results,
        crtsh_results,
        assetfinder_results,
        findomain_results
    )
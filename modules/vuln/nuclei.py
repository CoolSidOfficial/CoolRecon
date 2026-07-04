
from core.runner import run


def execute(hosts):
    """
    Vulnerability scanning using nuclei
    """

    input_data = "\n".join(hosts)

    command = f"echo '{input_data}' | nuclei -silent -severity low,medium,high,critical"

    return run(command)

import os


def save(domain, folder, filename, data):
    """
    Save results to:
    output/<domain>/<folder>/<filename>
    """

    path = os.path.join(
        "output",
        domain,
        folder
    )

    os.makedirs(
        path,
        exist_ok=True
    )

    file_path = os.path.join(
        path,
        filename
    )

    with open(file_path, "w") as file:
        file.write("\n".join(data))

    return file_path

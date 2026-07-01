import os


def save(domain, filename, data):

    path = f"output/{domain}"

    os.makedirs(
        path,
        exist_ok=True
    )


    file = f"{path}/{filename}.txt"


    with open(
        file,
        "w"
    ) as f:

        f.write(
            "\n".join(data)
        )


    return file
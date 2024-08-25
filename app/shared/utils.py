def read_file(path: str) -> str:
    with open(path,  "rb") as file:
        return file.read().decode("UTF-8")

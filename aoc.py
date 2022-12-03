from pathlib import Path

def read_data(day, file_name):
    with open(Path(str(day)) / file_name, "r") as f:
        data = f.read()
    return data
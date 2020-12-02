from pathlib import Path


def read_input(day, name):
    BASE_DIR = Path(__file__).parent
    input_path = BASE_DIR.joinpath('input', day, name)

    with open(input_path) as f:
        return f.readlines()
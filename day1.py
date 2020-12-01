from pathlib import Path
from typing import List


def get_input(path):
    with open(path) as f:
        return [int(line) for line in f.readlines()]


def solver(total, seq):
    # find the two entries that sum to total
    for i, num in enumerate(seq):
        if (total - num) in seq[i:]:
            return num, total - num
    else:
        raise Exception('can not solve')


def solve_part_one(total, seq):
    num_a, num_b = solver(total, seq)
    return num_a * num_b


def solve_part_two(total, seq):
    # find the three entries that sum to total
    for i, num_a in enumerate(seq):
        try:
            num_b, num_c = solver(total - num_a, seq[i:])
            return num_a * num_b * num_c
        except:
            pass


def main():
    BASE_DIR = Path(__file__).parent
    input_path = BASE_DIR.joinpath('input', 'day1', 'input.txt')
    test_path = BASE_DIR.joinpath('input', 'day1', 'test.txt')
    total = 2020

    input_seq = get_input(input_path)
    test_seq = get_input(test_path)

    assert solve_part_one(total, test_seq) == 514579
    print('part one result: ', solve_part_one(total, input_seq))

    assert solve_part_two(total, test_seq) == 241861950
    print('part two result: ', solve_part_two(total, input_seq))


if __name__ == "__main__":
    main()
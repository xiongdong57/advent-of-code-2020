import re

from utils import read_input


def is_valid(line, valid_func):
    lowest, highest, char, pwd = re.findall(r'(\d+)-(\d+) (\w+): (\w+)', line)[0]
    lowest = int(lowest)
    highest = int(highest)

    return valid_func(lowest, highest, char, pwd)


def valid_part_one(lowest, highest, char, pwd):
    return lowest <= pwd.count(char) <= highest


def valid_part_two(lowest, highest, char, pwd):
    return ((pwd[lowest - 1] + pwd[highest - 1]).count(char) == 1 
            if len(pwd) >= max(highest, lowest) else False)


def solve_part_one(seq):
    return sum(is_valid(line, valid_part_one) for line in seq)


def solve_part_two(seq):
    return sum(is_valid(line, valid_part_two) for line in seq)


def main():
    input_seq = read_input('day2', 'input.txt')
    test_seq = read_input('day2', 'test.txt')

    assert solve_part_one(test_seq)==2
    print('part one result: ', solve_part_one(input_seq))

    assert solve_part_two(test_seq) == 1
    print('part two result: ', solve_part_two(input_seq))


if __name__ == "__main__":
    main()
from utils import read_input
import re


def count_answers_p1(group):
    group = ''.join(group.split('\n'))
    return len(set(group))


def count_answers_p2(group):
    group_seq = group.split('\n')
    common = set(group_seq[0]).intersection(*group_seq)
    return len(common)


def solve_part_one(seq):
    groups = ''.join(seq).split('\n\n')
    return sum(count_answers_p1(group) for group in groups)


def solve_part_two(seq):
    groups = ''.join(seq).split('\n\n')
    return sum(count_answers_p2(group) for group in groups)


def main():
    input_seq = read_input('day6', 'input.txt')
    test_seq = read_input('day6', 'test.txt')

    assert solve_part_one(test_seq) == 11
    print('part one result: ', solve_part_one(input_seq))

    assert solve_part_two(test_seq) == 6
    print('part two result: ', solve_part_two(input_seq))


if __name__ == "__main__":
    main()

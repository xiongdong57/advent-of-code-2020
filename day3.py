from functools import reduce

from utils import read_input


def get_loc(x, y, i, line):
    index = y / x * i
    if int(index * 10) % 10 == 5:
        # 斜率包含0.5时，跳过奇数行（既不会碰到#，也不会碰到.)
        return
    index = int(index)
    mark = (line * ((index + 1) // len(line) + 1))[index]

    return 'O' if mark == '.' else 'X'


def solve_part_one(start_slope, seq):
    x, y = start_slope
    seq = [each.strip() for each in seq]
    tree = [get_loc(x, y, i, line) for i, line in enumerate(seq)]

    return tree.count('X')


def solve_part_two(seq):
    start_slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

    trees = [solve_part_one(start_slope, seq) for start_slope in start_slopes]
    return reduce(lambda x, y: x * y, trees)


def main():
    input_seq = read_input('day3', 'input.txt')
    test_seq = read_input('day3', 'test.txt')

    assert solve_part_one((1, 3), test_seq) == 7
    print('part one result: ', solve_part_one((1, 3), input_seq))

    assert solve_part_two(test_seq) == 336
    print('part two result: ', solve_part_two(input_seq))


if __name__ == "__main__":
    main()

from utils import read_input


def find_break(seq, num):
    for i, elem in enumerate(seq[num:]):
        if elem not in num_sums(seq[i + num - num: i + num]):
            return elem


def num_sums(seq):
    return [x + y for x in seq for y in seq if x != y]


def solve_part_one(seq, preamble_num):
    seq = [int(each) for each in seq]
    return find_break(seq, preamble_num)


def solve_part_two(seq, num):
    seq = [int(each) for each in seq]
    break_num = solve_part_one(seq, num)
    for x in range(len(seq)):
        for y in range(x + 1, len(seq)):
            if sum(seq[x:y]) == break_num:
                return max(seq[x: y]) + min(seq[x: y])


def main():
    input_seq = read_input('day9', 'input.txt')
    test_seq = read_input('day9', 'test.txt')

    assert solve_part_one(test_seq, 5) == 127
    print('part one result: ', solve_part_one(input_seq, 25))

    assert solve_part_two(test_seq, 5) == 62
    print('part two result: ', solve_part_two(input_seq, 25))


if __name__ == "__main__":
    main()

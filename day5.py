from utils import read_input


def locate(bin):
    row = locate_row(bin[:7])
    column = locate_column(bin[-3:])
    return row * 8 + column


def locate_row(bin):
    return sum(2 ** (6 - i) for i, char in enumerate(bin) if char == 'B')


def locate_column(bin):
    return sum(2 ** (2 - i) for i, char in enumerate(bin) if char == 'R')


def solve_part_one(seq):
    return max(locate(board.strip()) for board in seq)


def solve_part_two(seq):
    located_ids = set(locate(board.strip()) for board in seq)
    free_ids = set(i * 8 + j for i in range(127) for j in range(7)) - \
        located_ids

    for c_id in free_ids:
        if ((c_id - 1) in located_ids) & ((c_id + 1) in located_ids):
            return c_id


def main():
    input_seq = read_input('day5', 'input.txt')
    test_seq = read_input('day5', 'test.txt')

    assert solve_part_one(test_seq) == 820
    print('part one result: ', solve_part_one(input_seq))

    print('part two rsult: ', solve_part_two(input_seq))


if __name__ == "__main__":
    main()

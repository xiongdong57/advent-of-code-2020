from utils import read_input


def gen_spoken(seq):
    last_num = seq[-1]
    spokens = seq[:-1]

    if last_num not in spokens:
        return 0

    return spokens[::-1].index(last_num) + 1


def solve_part_one(seq):
    seq = [int(num) for num in seq[0].strip().split(',')]
    for i in range(0, 2020):
        if i < len(seq):
            pass
        spoken = gen_spoken(seq)
        seq.append(spoken)
    return seq[2019]


def solve_part_two(seq):
    seq = [int(num) for num in seq[0].strip().split(',')]
    mem = {e: i for i, e in enumerate(seq[:-1])}
    for i in range(len(seq) - 1, 30000000):
        last_num = seq[-1]
        if last_num not in mem:
            mem[seq[i - 1]] = i - 1
            seq.append(0)
        else:
            mem[seq[i - 1]] = i - 1
            seq.append(i - mem[last_num])
    return seq[30000000 - 1]


def main():
    input_seq = read_input('day15', 'input.txt')
    test_seq = read_input('day15', 'test.txt')

    assert solve_part_one(test_seq) == 436
    print('part one result: ', solve_part_one(input_seq))

    assert solve_part_two(test_seq) == 175594
    print('part two result: ', solve_part_two(input_seq))


if __name__ == "__main__":
    main()

def parse_subject_num(num):
    i = 1
    count_num = 0
    while (i != num):
        i *= 7
        i %= 20201227
        count_num += 1
    return count_num


def encryption(public_key, size):
    key = public_key
    i = 1
    for _ in range(size):
        i *= key
        i %= 20201227
    return i


def solve_part_one(seq):
    card_loop_size = parse_subject_num(seq[0])

    return encryption(seq[1], card_loop_size)


def main():
    input_seq = [19241437, 17346587]
    test_seq = [5764801, 17807724]

    assert solve_part_one(test_seq) == 14897079
    print('part one result: ', solve_part_one(input_seq))


if __name__ == "__main__":
    main()

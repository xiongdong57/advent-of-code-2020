import re
from itertools import product

from utils import read_input


def parse(seq):
    res = []
    for line in seq:
        if 'mask' in line:
            res.append(('mask', line.strip()[7:]))
        else:
            addr, value = re.findall(r'(\d+)', line)
            res.append((int(addr), int(value)))
    return res


def mask_map(mask, value):
    bin_value = bin(value)[2:].zfill(36)
    res = ''
    for m, v in zip(mask, bin_value):
        if m == 'X':
            res += v
        else:
            res += m
    return int(res, 2)


def run(seq):
    mem = {}
    _, mask = seq[0]
    for step in seq[1:]:
        if 'mask' in step:
            _, mask = step
        else:
            addr, value = step
            mem[addr] = mask_map(mask, value)
    return mem


def solve_part_one(seq):
    seq = parse(seq)
    mem = run(seq)
    return sum(v for k, v in mem.items())


def mask_map_p2(mask, value):
    # gen 000000000000000000000000000000X1101X, then map to possible value
    bin_value = bin(value)[2:].zfill(36)
    res = ''
    for m, v in zip(mask, bin_value):
        if m == 'X':
            res += 'X'
        elif m == '0':
            res += v
        else:
            res += m

    for chances in product('10', repeat=res.count('X')):
        tmp = res
        for char in chances:
            tmp = tmp.replace('X', char, 1)
        yield int(tmp, 2)


def run_p2(seq):
    mem = {}
    _, mask = seq[0]
    for step in seq[1:]:
        if 'mask' in step:
            _, mask = step
        else:
            address, value = step
            for addr in mask_map_p2(mask, address):
                mem[addr] = value
    return mem


def solve_part_two(seq):
    seq = parse(seq)
    mem = run_p2(seq)
    return sum(v for k, v in mem.items())


def main():
    input_seq = read_input('day14', 'input.txt')
    test_seq = read_input('day14', 'test.txt')

    assert solve_part_one(test_seq) == 165
    print('part one result: ', solve_part_one(input_seq))

    assert solve_part_two(read_input('day14', 'test_p2.txt')) == 208
    print('part two result: ', solve_part_two(input_seq))


if __name__ == "__main__":
    main()

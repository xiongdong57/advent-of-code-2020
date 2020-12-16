import re
from collections import defaultdict

from utils import read_input


def parse(seq):
    seq = ''.join(seq).split('\n\n')
    rules = {re.findall(r'(.*?):', line)[0]:
             re.findall(r'(\d+)-(\d+)', line)
             for line in seq[0].split('\n')}

    tickets = seq[1].split('\n')[1].split(',')
    nearbys = [line.split(',') for line in seq[2].split('\n')[1:]]
    return rules, tickets, nearbys


def valid_num(rules, num):
    for k, r in rules.items():
        for num1, num2 in r:
            if int(num1) <= int(num) <= int(num2):
                return True
    return False


def valid_ticket(rules, ticket):
    return all(valid_num(rules, num) for num in ticket)


def solve_part_one(seq):
    rules, ticket, nearbys = parse(seq)
    res = 0
    for nearby in nearbys:
        for num in nearby:
            if not valid_num(rules, num):
                res += int(num)
    return res


def solve(mem):
    if all(len(v) == 1 for k, v in mem.items()):
        return mem
    values = [v for k, v in mem.items() if len(v) == 1]
    for value in values:
        for k, v in mem.items():
            if v != value:
                mem.update({k: v - value})
    return solve(mem.copy())


def solve_part_two(seq):
    rules, ticket, nearbys = parse(seq)
    nearbys = [ticket for ticket in nearbys if valid_ticket(rules, ticket)]
    mem = defaultdict(set)

    for name, rule in rules.items():
        for i, col in enumerate(zip(*nearbys)):
            if valid_ticket({name: rule}, col):
                mem[name].add(i)

    mapping = solve(mem)
    res = 1
    for key, value in mapping.items():
        if 'departure' in key:
            res *= int(ticket[value.pop()])
    return res


def main():
    input_seq = read_input('day16', 'input.txt')
    test_seq = read_input('day16', 'test.txt')

    assert solve_part_one(test_seq) == 71
    print('part one result: ', solve_part_one(input_seq))

    print('part two result: ', solve_part_two(input_seq))


if __name__ == "__main__":
    main()

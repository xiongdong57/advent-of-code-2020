from utils import read_input
import re


def parse(seq):
    seq = ''.join(seq).replace('"', '').split('\n\n')
    rules = dict()
    for line in seq[0].split('\n'):
        name, rule = re.findall(r'(\d+): (.*)', line)[0]
        rules[name] = rule
    messages = seq[1].split('\n')
    return rules, messages


def gen_syntax(rules, root):
    nums = root.split(' ')
    for num in nums:
        if num in rules:
            new_rule = ' ' + rules[num] + ' '
            if '|' in new_rule:
                new_rule = ' ( ' + new_rule + ' ) '
            root = re.sub(f' {num} ', new_rule, root)
    if any(char in root for char in '0123456789'):
        return gen_syntax(rules, root)
    else:
        root = '^' + root.replace(' ', '') + '$'
        return root


def solve_part_one(seq):
    rules, messages = parse(seq)
    root = ' ' + rules['0'] + ' '
    syn = gen_syntax(rules, root)
    re_complier = re.compile(syn)
    num = 0
    for m in messages:
        if re_complier.match(m):
            num += 1
    return num


def valid(rules, message):
    # rule 8 will be 42+
    # since rule 11 is 42 31, rule will be 42{x}31{x}, x is 1 to infinite
    # since rule 42 /31 a least match 5 chars (count manually)
    # if message is short, return False
    rules['8'] = '42 +'
    x = 1
    while len(message) // 10 >= x:
        rules['11'] = str('42 ' * x + '31 ' * x)[:-1]
        syn = gen_syntax(rules, ' ' + rules['0'] + ' ')
        if re.match(syn, message):
            return True
        x += 1
    return False


def solve_part_two(seq):
    rules, messages = parse(seq)
    num = 0
    for m in messages:
        if valid(rules, m):
            num += 1
    return num


def main():
    input_seq = read_input('day19', 'input.txt')
    test_seq = read_input('day19', 'test.txt')

    assert solve_part_one(test_seq) == 2
    print('part one result: ', solve_part_one(input_seq))

    assert solve_part_two(read_input('day19', 'test_p2.txt')) == 12
    print('part two result: ', solve_part_two(input_seq))


if __name__ == "__main__":
    main()

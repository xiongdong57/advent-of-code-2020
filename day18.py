from utils import read_input
import re


def calcator_p1(exp):
    # expressions without Parentheses
    exp = exp.split(' ')
    num = int(exp[0])
    operator = ''
    for elem in exp[1:]:
        if elem in ('*', '+'):
            operator = elem
        else:
            if operator == '*':
                num *= int(elem)
            elif operator == '+':
                num += int(elem)
    return num


def calcator_p2(exp):
    exp = exp.split(' ')
    if '+' in exp:
        loc = exp.index('+')
        tmp = int(exp[loc - 1]) + int(exp[loc + 1])
        new_exp = ' '.join(
            exp[:loc - 1] + [str(tmp)] + exp[loc + 2:])
        return calcator_p2(new_exp)
    else:
        num = int(exp[0])
        for elem in exp[1:]:
            if elem != '*':
                num *= int(elem)
        return num


def evaluate(exp, calc):
    if '(' not in exp:
        return calc(exp)
    num = 0
    end = 0
    start = exp.index('(')
    for i, elem in enumerate(exp):
        if elem == '(':
            num += 1
        elif elem == ')':
            num -= 1
            if num == 0:
                end = i
                break
    sub_exp = evaluate(exp[start + 1: end], calc)
    new_exp = exp[:start] + str(sub_exp) + exp[end + 1:]
    return evaluate(new_exp, calc)


def solve_part_one(seq):
    return sum(evaluate(m.strip(), calcator_p1) for m in seq)


def solve_part_two(seq):
    return sum(evaluate(m.strip(), calcator_p2) for m in seq)


def main():
    input_seq = read_input('day18', 'input.txt')

    print('part one result: ', solve_part_one(input_seq))
    print('part two result: ', solve_part_two(input_seq))


if __name__ == "__main__":
    main()

from utils import read_input


def parse(seq):
    return [[line[:3], int(line[3:])] for line in seq]


def execute(program, ticker, acc, visited):
    if ticker >= len(program):
        return acc, 'finite'

    operation, num = program[ticker][0], program[ticker][1]
    if ticker in visited:
        return acc, 'infinite'

    if operation == 'acc':
        return execute(program, ticker + 1, acc + num, visited + [ticker])
    if operation == 'jmp':
        return execute(program, ticker + num, acc, visited + [ticker])
    if operation == 'nop':
        return execute(program, ticker + 1, acc, visited + [ticker])


def solve_part_one(seq):
    program = parse(seq)
    return execute(program, 0, 0, [])[0]


def fix_program(program):
    for i, elem in enumerate(program):
        tmp_program = program
        if elem[0] == 'acc':
            continue
        elif elem[0] == 'jmp':
            tmp_program = program[:i] + [['nop', elem[1]]] + program[i+1:]
        elif elem[0] == 'nop':
            tmp_program = program[:i] + [['jmp', elem[1]]] + program[i+1:]

        acc, finite_mark = execute(tmp_program, 0, 0, [])
        if finite_mark == 'finite':
            return acc


def solve_part_two(seq):
    program = parse(seq)
    return fix_program(program)


def main():
    input_seq = read_input('day8', 'input.txt')
    test_seq = read_input('day8', 'test.txt')

    assert solve_part_one(test_seq) == 5
    print('part one result: ', solve_part_one(input_seq))

    assert solve_part_two(test_seq) == 8
    print('part two result: ', solve_part_two(input_seq))


if __name__ == "__main__":
    main()

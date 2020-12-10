from utils import read_input


def run(seq, ticker, res):
    if len(seq) == 1:
        return res + seq + [seq[0] + 3]
    new_ticker = min(ticker + i for i in range(1, 4) if (ticker + i) in seq)
    seq.remove(new_ticker)

    return run(seq, new_ticker, res + [new_ticker])


def find_diff(seq):
    counter = [elem - seq[i] for i, elem in enumerate(seq[1:])]
    return counter.count(1) * counter.count(3)


def solve_part_one(seq):
    seq = [int(elem) for elem in seq]
    diffs = run(seq, 0, [0])
    return find_diff(diffs)


def solve_part_two(seq):
    seq = [int(elem) for elem in seq]
    diffs = run(seq, 0, [0])
    node_path_seq = []
    continus_count = False
    num_path = 1
    mul = 1
    for i, elem in enumerate(diffs):
        # node_path_count 代表当前节点，跳过上一个节点和之前两个节点可能的连接数
        node_path_count = 1
        if (elem - 2) in diffs[:i - 1]:
            node_path_count += node_path_seq[i - 2]
        elif (elem - 3) in diffs[:i - 1]:
            node_path_count += node_path_seq[i - 3]
        node_path_seq.append(node_path_count)

        # node_path_seq 计算最终可能连接数，连续大于 1 的数字相加，乘之前的连接数
        if node_path_count == 1:
            if continus_count:
                num_path *= mul
            continus_count = False
            mul = 1
        else:
            mul += node_path_count - (0 if continus_count else 1)
            continus_count = True

    return num_path


def main():
    input_seq = read_input('day10', 'input.txt')
    test_seq = read_input('day10', 'test.txt')

    assert solve_part_one(test_seq) == 220
    print('part one result: ', solve_part_one(input_seq))

    assert solve_part_two(test_seq) == 19208
    print('part two result: ', solve_part_two(input_seq))


if __name__ == "__main__":
    main()

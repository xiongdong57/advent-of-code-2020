from utils import read_input


def solve_part_one(seq):
    earliest_time = int(seq[0])
    buses = [int(bus) for bus in seq[1].split(',') if bus != 'x']
    res = []
    for bus in buses:
        wait = (earliest_time // bus + 1) * bus - earliest_time
        res.append((wait, bus))
    min_wait, bus_num = min(res)
    return min_wait * bus_num


def solve_part_two(seq):
    # 这个解法是从其它地方看到的，并没有理解计算原理.
    def bezout(a, b):
        if a - b == 1:
            return 1, -1
        q, r = a // b, a % b
        m, n = bezout(b, r)
        return n, m - n * q

    buses_time = [(int(bus), -i) for (i, bus) in enumerate(seq[1].split(','))
                  if bus != 'x']

    prod = 1
    for b, _ in buses_time:
        prod *= b

    ans = 0
    for b, i in buses_time:
        m, n = bezout(prod // b, b)
        ans += i % b * m * prod // b

    return ans % prod


def main():
    input_seq = read_input('day13', 'input.txt')
    test_seq = read_input('day13', 'test.txt')

    assert solve_part_one(test_seq) == 295
    print('part one result: ', solve_part_one(input_seq))

    assert solve_part_two(test_seq) == 1068781
    print('part two result: ', solve_part_two(input_seq))


if __name__ == "__main__":
    main()

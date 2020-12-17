from utils import read_input
from itertools import product


def print_map(whole_map, n):
    for z in range(- n, n + 1):
        for x in range(-1 - n, 2 + n):
            print(''.join(whole_map[(x, y, z)] for y in range(-1 - n, 2 + n)))
        print('\n')


def count_active_neighbors_p1(whole_map, point):
    x1, y1, z1 = point
    active_nergbors = -1 if whole_map[point] == '#' else 0
    for x, y, z in product([-1, 0, 1], repeat=3):
        neighbor = (x1 + x, y1 + y, z1 + z)
        if whole_map.get(neighbor) == '#':
            active_nergbors += 1
    return active_nergbors


def count_active_neighbors_p2(whole_map, point):
    x1, y1, z1, i1 = point
    active_nergbors = -1 if whole_map[point] == '#' else 0
    for x, y, z, i in product([-1, 0, 1], repeat=4):
        neighbor = (x1 + x, y1 + y, z1 + z, i1 + i)
        if whole_map.get(neighbor) == '#':
            active_nergbors += 1
    return active_nergbors


def update(whole_map, count_active):
    new_map = {}
    for k, v in whole_map.items():
        if v == '#' and count_active(whole_map, k) in (2, 3):
            new_map[k] = '#'
        elif v == '.' and count_active(whole_map, k) == 3:
            new_map[k] = '#'
        else:
            new_map[k] = '.'
    return new_map


def solve_part_one(seq):
    board = len(seq) // 2
    reminder = len(seq) % 2
    n = 6
    whole_map = {(x, y, z): '.'
                 for x in range(- board - n, board + n + 1)
                 for y in range(- board - n, board + n + 1)
                 for z in range(- n, n + 1)}

    # initial
    for x in range(-board, board + reminder):
        for y in range(-board, board + reminder):
            whole_map[(x, y, 0)] = seq[x + board][y + board]
    new_map = whole_map.copy()

    # update
    for i in range(n):
        new_map = update(new_map, count_active_neighbors_p1)
    return [v for k, v in new_map.items()].count('#')


def solve_part_two(seq):
    board = len(seq) // 2
    reminder = len(seq) % 2
    n = 6
    whole_map = {(x, y, z, i): '.'
                 for x in range(- board - n, board + n + 1)
                 for y in range(- board - n, board + n + 1)
                 for z in range(- n, n + 1)
                 for i in range(- n, n + 1)}

    # initial
    for x in range(-board, board + reminder):
        for y in range(-board, board + reminder):
            whole_map[(x, y, 0, 0)] = seq[x + board][y + board]
    new_map = whole_map.copy()

    # update
    for i in range(n):
        new_map = update(new_map, count_active_neighbors_p2)
    return [v for k, v in new_map.items()].count('#')


def main():
    input_seq = read_input('day17', 'input.txt')
    test_seq = read_input('day17', 'test.txt')

    assert solve_part_one(test_seq) == 112
    print('part one result: ', solve_part_one(input_seq))

    assert solve_part_two(test_seq) == 848
    print('part two result: ', solve_part_two(input_seq))


if __name__ == "__main__":
    main()

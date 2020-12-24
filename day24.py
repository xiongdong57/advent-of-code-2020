from utils import read_input
from collections import Counter


def parse(seq):
    # e, se, sw, w, nw, ne is valid
    prev = ''
    for elem in seq.strip():
        if elem in ('s', 'n'):
            prev = elem
        else:
            yield prev + elem
            prev = ''


def move_once(start, action):
    translator = {
        'e': (2, 0),
        'se': (1, -1),
        'sw': (-1, -1),
        'w': (-2, 0),
        'nw': (-1, 1),
        'ne': (1, 1)
    }
    x, y = start
    dx, dy = translator[action]

    return (x + dx, y + dy)


def get_loc(seq):
    loc = (0, 0)
    for action in parse(seq.strip()):
        loc = move_once(loc, action)
    return loc


def solve_part_one(seq):
    res = [get_loc(line) for line in seq]
    num_count = Counter(res)
    return sum(num % 2 for num in num_count.values())


def count_adjacent(loc, black_tiles):
    adjacents = [(2, 0), (1, -1), (-1, -1), (-2, 0), (-1, 1), (1, 1)]
    return sum(1
               if (loc[0] + dx, loc[1] + dy) in black_tiles else 0
               for (dx, dy) in adjacents)


def simulator(black_tiles):
    new_black_tiles = set()
    white_to_explore = set()

    for loc in black_tiles:
        num_black_adjacents = count_adjacent(loc, black_tiles)
        if 0 < num_black_adjacents <= 2:
            new_black_tiles.add(loc)

        adjacents = [(2, 0), (1, -1), (-1, -1), (-2, 0), (-1, 1), (1, 1)]
        for (dx, dy) in adjacents:
            new_loc = (dx + loc[0], dy + loc[1])
            if new_loc not in black_tiles:
                white_to_explore.add(new_loc)

    for loc in white_to_explore:
        num_black_adjacents = count_adjacent(loc, black_tiles)
        if num_black_adjacents == 2:
            new_black_tiles.add(loc)

    return new_black_tiles


def solve_part_two(seq):
    res = [get_loc(line) for line in seq]
    num_count = Counter(res)
    black_tiles = set(key for key in num_count if num_count[key] % 2)
    for _ in range(100):
        black_tiles = simulator(black_tiles)
    return len(black_tiles)


def main():
    input_seq = read_input('day24', 'input.txt')
    test_seq = read_input('day24', 'test.txt')

    assert solve_part_one(test_seq) == 10
    print('part one result: ', solve_part_one(input_seq))

    assert solve_part_two(test_seq) == 2208
    print('part two result: ', solve_part_two(input_seq))


if __name__ == "__main__":
    main()

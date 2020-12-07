import re

from utils import read_input


def parse(seq):
    bag_map = {}
    for line in seq:
        key = re.findall(r'^(.+? bag)', line)[0]
        bag_map[key] = {bag: int(count) for count, bag in re.findall(
            r'(\d+) (.+? bag)', line)}
    return bag_map


def find_bag(bag, bag_map, goal):
    bag_contains = bag_map[bag].keys()
    if bag_contains:
        if goal in bag_contains:
            return True
        return any(find_bag(b, bag_map, goal) for b in bag_contains)
    return False


def solve_part_one(seq):
    goal = 'shiny gold bag'
    bag_map = parse(seq)

    return sum(find_bag(bag, bag_map, goal) for bag in bag_map.keys())


def count_bag(bag, bag_map):
    bag_contains = bag_map[bag]
    if bag_contains:
        return sum(
            count * (count_bag(b, bag_map) + 1)
            for b, count in bag_contains.items())

    return 0


def solve_part_two(seq):
    goal = 'shiny gold bag'
    bag_map = parse(seq)

    return count_bag(goal, bag_map)


def main():
    input_seq = read_input('day7', 'input.txt')
    test_seq = read_input('day7', 'test.txt')

    assert solve_part_one(test_seq) == 4
    print('part one result: ', solve_part_one(input_seq))

    assert solve_part_two(read_input('day7', 'test_p2.txt')) == 126
    print('part two result: ', solve_part_two(input_seq))


if __name__ == "__main__":
    main()

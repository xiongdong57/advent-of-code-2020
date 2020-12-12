from utils import read_input


def count_adjacent(layout, row, column, x, y):
    new_r = row + x
    new_c = column + y

    if (new_r < 0 or new_c < 0 or new_r >= len(layout) or
       new_c >= len(layout[0])):
        return 0

    return 1 if layout[new_r][new_c] == '#' else 0


def count_occupied(layout, row, column, count_func):
    return (count_func(layout, row, column, 0, 1) +
            count_func(layout, row, column, 0, -1) +
            count_func(layout, row, column, 1, 1) +
            count_func(layout, row, column, 1, -1) +
            count_func(layout, row, column, -1, 1) +
            count_func(layout, row, column, -1, -1) +
            count_func(layout, row, column, 1, 0) +
            count_func(layout, row, column, -1, 0))


def count_direction(layout, row, column, x, y):
    new_r = row + x
    new_c = column + y

    if (new_r < 0 or new_c < 0 or new_r >= len(layout) or
       new_c >= len(layout[0])):
        return 0

    if layout[new_r][new_c] == 'L':
        return 0

    if layout[new_r][new_c] == '#':
        return 1

    if layout[new_r][new_c] == '.':
        return count_direction(layout, new_r, new_c, x, y)


def transfer(layout, occupied_to_empty, count_func):
    seats = [e[:] for e in layout]
    for row in range(len(seats)):
        for column in range(len(seats[row])):
            if ((layout[row][column] == 'L') &
               (count_occupied(layout, row, column, count_func) == 0)):
                seats[row][column] = '#'
            if ((layout[row][column] == '#') &
               (count_occupied(layout, row, column, count_func) >=
               occupied_to_empty)):
                seats[row][column] = 'L'
    return seats


def solve_part_one(seq):
    previous = [list(each.strip()) for each in seq]
    while True:
        seats = transfer(previous, 4, count_adjacent)
        if seats == previous:
            break
        else:
            previous = [e[:] for e in seats]

    return sum(each.count('#') for each in seats)


def solve_part_two(seq):
    previous = [list(each.strip()) for each in seq]
    while True:
        seats = transfer(previous, 5, count_direction)
        if seats == previous:
            break
        else:
            previous = [e[:] for e in seats]
    return sum(each.count('#') for each in seats)


def main():
    input_seq = read_input('day11', 'input.txt')
    test_seq = read_input('day11', 'test.txt')

    assert solve_part_one(test_seq) == 37
    print('part one result: ', solve_part_one(input_seq))

    assert solve_part_two(test_seq) == 26
    print('part two result: ', solve_part_two(input_seq))


if __name__ == "__main__":
    main()

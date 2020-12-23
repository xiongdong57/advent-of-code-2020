from typing import List


def find_dest(crr_cup: int, picks: List, clock: List):
    if crr_cup <= 1:
        return max(clock)
    if crr_cup - 1 not in picks:
        return crr_cup - 1
    return find_dest(crr_cup - 1, picks, clock)


def game(clock: List, crr_cup: int, length: int):
    crr_index = clock.index(crr_cup)
    next_cup = clock[(crr_index + 4) % length]

    picks = [clock[(crr_index + i) % length] for i in range(1, 4)]
    for elem in picks:
        clock.remove(elem)

    dest = find_dest(crr_cup, picks, clock)

    dest_index = clock.index(dest)
    for elem in picks[::-1]:
        clock.insert((dest_index + 1) % length, elem)
    return next_cup, clock


def solve_part_one(seq):
    clock = seq.copy()
    crr_cup = clock[0]
    length = len(clock)
    for _ in range(100):
        crr_cup, clock = game(clock, crr_cup, length)

    start = clock.index(1)
    return ''.join(map(str, clock[start+1:] + clock[:start]))


def play_game(cups, rounds):
    circle = dict(zip(cups, cups[1:] + cups[:1]))
    current_label = cups[-1]
    for r in range(rounds):
        current_label = circle[current_label]
        picks = []
        tmp_label = current_label
        for _ in range(3):
            tmp_label = circle[tmp_label]
            picks.append(tmp_label)
        circle[current_label] = circle[tmp_label]

        dest_label = current_label - 1
        while dest_label in picks or dest_label < 1:
            dest_label -= 1
            if dest_label < 1:
                dest_label = max(cups)

        circle[dest_label], circle[picks[-1]] = picks[0], circle[dest_label]
    return circle


def solve_part_two(seq):
    # I know nothing about linked list.
    # this is somebody's solution
    cups_p2 = seq + list(range(10, int(1e6) + 1))
    circle = play_game(cups_p2, int(1e7))
    # print(circle)
    ans = 1
    next_elem = 1
    for _ in range(2):
        next_elem = circle[next_elem]
        ans *= next_elem
    return ans


def main():
    input_seq = [1, 3, 5, 4, 6, 8, 7, 2, 9]
    test_seq = [3, 8, 9, 1, 2, 5, 4, 6, 7]

    assert solve_part_one(test_seq) == '67384529'
    print('part one result: ', solve_part_one(input_seq))

    assert solve_part_two(test_seq) == 149245887792
    print('part two result: ', solve_part_two(input_seq))


if __name__ == "__main__":
    main()

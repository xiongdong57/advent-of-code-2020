from utils import read_input


def parse(seq):
    players = ''.join(seq).split('\n\n')
    player_A = list(map(int, players[0].split('\n')[1:]))
    player_B = list(map(int, players[1].split('\n')[1:]))
    return player_A, player_B


def game(p_A, p_B):
    if not p_A or (not p_B):
        return p_A, p_B
    card_a = p_A.pop(0)
    card_b = p_B.pop(0)
    if card_a > card_b:
        p_A += [card_a, card_b]
    else:
        p_B += [card_b, card_a]
    return game(p_A, p_B)


def solve_part_one(seq):
    player_A, player_B = parse(seq)
    p_A, p_B = game(player_A.copy(), player_B.copy())
    final = p_A if p_A else p_B
    return sum((i + 1) * num for i, num in enumerate(final[::-1]))


def recursive_game(p_A, p_B):
    # 修改成bfs
    seen = list()
    winner = None
    while len(p_A) and len(p_B):
        if (p_A, p_B) in seen:
            return 'a', p_A, p_B
        seen.append((p_A.copy(), p_B.copy()))

        card_a = p_A.pop(0)
        card_b = p_B.pop(0)

        if len(p_A) >= card_a and len(p_B) >= card_b:
            winner, _, _ = recursive_game(
                p_A[:card_a].copy(), p_B[:card_b].copy())
        else:
            winner = 'a' if card_a > card_b else 'b'

        if winner == 'a':
            p_A += [card_a, card_b]
        else:
            p_B += [card_b, card_a]

    return winner, p_A, p_B


def solve_part_two(seq):
    player_A, player_B = parse(seq)
    winner, pa, pb = recursive_game(player_A.copy(), player_B.copy())
    final = pa if winner == 'a' else pb
    return sum((i + 1) * num for i, num in enumerate(final[::-1]))


def main():
    input_seq = read_input('day22', 'input.txt')
    test_seq = read_input('day22', 'test.txt')

    assert solve_part_one(test_seq) == 306
    print('part one result: ', solve_part_one(input_seq))

    assert solve_part_two(test_seq) == 291
    print('part two result: ', solve_part_two(input_seq))


if __name__ == "__main__":
    main()

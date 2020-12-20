from utils import read_input
from collections import defaultdict
from itertools import combinations
from functools import reduce
import math
import numpy as np


def parse(seq):
    tiles = defaultdict(list)
    for tile in ''.join(seq).split('\n\n'):
        lines = tile.split('\n')
        key = lines[0][5:9]
        for line in lines[1:]:
            tiles[key].append(list(line))
    return tiles


def edge_line(tile):
    top = tile[0]
    bottom = tile[-1]
    left = [elem[0] for elem in tile]
    right = [elem[-1] for elem in tile]

    return [top, bottom, left, right,
            top[::-1], bottom[::-1], left[::-1], right[::-1]]


def count_common_line(tile_x, tile_y):
    x_lines = edge_line(tile_x)
    y_lines = edge_line(tile_y)[:4]
    return sum(1 for line in x_lines if line in y_lines)


def solve_part_one(seq):
    tiles = parse(seq)
    nodes = defaultdict(dict)
    for t1, t2 in combinations(tiles.keys(), 2):
        common = count_common_line(tiles[t1], tiles[t2])
        if common > 0:
            nodes[t1][t2] = common
            nodes[t2][t1] = common
    corners = [k for k, v in nodes.items() if len(v) == 2]
    return reduce(lambda x, y: x * y, map(int, corners))


def solve(nodes, graph):
    if all(v for _, v in graph.items()):
        return graph
    for key in graph:
        if not graph[key]:
            possible = get_possibility(nodes, graph, key)
            if possible:
                possible = reduce(lambda x, y: x.intersection(y),
                                  possible)
                if len(possible) == 1:
                    graph.update({key: possible.pop()})
                    break

    return solve(nodes, graph)


def get_possibility(nodes, graph, node):
    possible = []
    x, y = node
    for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        near = (x + dx, y + dy)
        if near in graph:
            near_tile = graph[near]
            possibility = set(nodes[near_tile]) - set(graph.values())
            if possibility:
                possible.append(possibility)
    return possible


def bulid_graph(nodes, corners, width):
    # init
    graph = {}
    for i in range(width):
        for j in range(width):
            graph[(i, j)] = None
    graph[(0, 0)] = corners[0]
    near = nodes[corners[0]]
    graph[(0, 1)] = near[0]
    graph[(1, 0)] = near[1]

    # dfs search to solve
    graph = solve(nodes, graph)

    return graph


def rotate_flips(tile):
    arr = np.array(tile)
    for rot in range(4):
        for flip in range(4):
            new_arr = np.rot90(arr, k=rot)
            new_arr = flip_arr(new_arr, flip)
            yield new_arr.tolist()


def flip_arr(arr, flip_flag):
    if flip_flag == 0:
        return arr
    if flip_flag == 1:
        return np.flip(arr)
    if flip_flag == 2:
        return np.flip(arr, 0)
    if flip_flag == 3:
        return np.flip(arr, 1)


def check_nearbys(tile, point, graph, tiles):
    for dp in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        yield fit_line(tile, point, dp, graph, tiles)


def fit_line(tile, point, dp, graph, tiles):
    x, y = point
    dx, dy = dp
    new_point = (x + dx, y + dy)
    if new_point not in graph:
        return True
    else:
        nearby_possible = edge_line(tiles[graph[new_point]])
        if dp == (0, -1):
            return [elem[0] for elem in tile] in nearby_possible
        if dp == (0, 1):
            return [elem[-1] for elem in tile] in nearby_possible
        if dp == (1, 0):
            return tile[-1] in nearby_possible
        if dp == (-1, 0):
            return tile[0] in nearby_possible


def valid_monster(monster, arr):
    return all(arr[i, j] == '#'
               for i in range(monster.shape[0])
               for j in range(monster.shape[1])
               if monster[i, j] == '#')


def solve_part_two(seq):
    # this is really a tough one, almost give up. until realize it could
    # be arranged first(without consider rotate).
    # then rotate/flip every tile to bulid the image. Numpy helps this.
    # Once the image is ready, find monster will not that hard.
    # tiles would be (num, style) pair
    tiles = parse(seq)
    nodes = defaultdict(list)
    for t1, t2 in combinations(tiles.keys(), 2):
        common = count_common_line(tiles[t1], tiles[t2])
        if common > 0:
            nodes[t1].append(t2)
            nodes[t2].append(t1)
    corners = [k for k, v in nodes.items() if len(v) == 2]
    width = int(math.sqrt(len(nodes)))

    # first bulid graph
    # graph would be {(0, 0): '2049'}, the (loc, tile-key) pair
    graph = bulid_graph(nodes, corners, width)

    # next rotate and flip every tile to fit
    # dot_graph would be {loc: style} pair
    dot_graph = {}
    for loc, key in graph.items():
        current_tile = tiles[key]
        for tile in rotate_flips(current_tile):
            if all(check_nearbys(tile, loc, graph, tiles)):
                dot_graph[loc] = tile

    # bulid image from dot_graph
    row_arrs = []
    for i in range(width):
        arrs = []
        for j in range(width):
            arr = np.array(dot_graph[(i, j)])
            arr = np.delete(arr, [0, 9], 1)
            arr = np.delete(arr, [0, 9], 0)
            arrs.append(arr)
        row_arrs.append(np.concatenate(tuple(arrs), axis=1))
    image = np.concatenate(tuple(row_arrs))

    # finally find monster
    monster = ("                  # ",
               "#    ##    ##    ###",
               " #  #  #  #  #  #   ",)
    monster = np.array([list(line) for line in monster])
    for img in rotate_flips(image):
        img = np.array(img)
        num_monster = 0
        for i in range(image.shape[0] - monster.shape[0] + 1):
            for j in range(image.shape[1] - monster.shape[1] + 1):
                # find monster
                if valid_monster(monster,
                   img[i: i + monster.shape[0], j: j + monster.shape[1]]):
                    num_monster += 1
        if num_monster > 0:
            return (image == '#').sum() - (monster == '#').sum() * num_monster


def main():
    input_seq = read_input('day20', 'input.txt')
    test_seq = read_input('day20', 'test.txt')

    assert solve_part_one(test_seq) == 20899048083289
    print('part one result: ', solve_part_one(input_seq))

    assert solve_part_two(test_seq) == 273
    print('part two result: ', solve_part_two(input_seq))


if __name__ == "__main__":
    main()

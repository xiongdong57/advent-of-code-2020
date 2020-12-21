from utils import read_input
import re
from collections import defaultdict
from functools import reduce


def parse(seq):
    # return {'dairy': [{'mxmxvkd', 'nhms'}, {'mxmxvkd','fvjkl'}]} pair
    allergen_graph = defaultdict(list)
    ingredients_seq = []
    for line in seq:
        ingredients, allergens = re.findall(
            r'(.*?) \(contains (.*?)\)', line)[0]
        ingredients_seq += ingredients.split(' ')
        for allergen in allergens.split(', '):
            allergen_graph[allergen].append(set(ingredients.split(' ')))
    return allergen_graph, ingredients_seq


def solve(graph):
    if all(len(v) == 1 for k, v in graph.items()):
        return {k: v.pop() for k, v in graph.items()}
    for k, v in graph.items():
        if isinstance(v, list):
            graph[k] = reduce(lambda x, y: x.intersection(y), v)
    solved_nodes = [k for k, v in graph.items() if len(v) == 1]
    for node in solved_nodes:
        # value will be a set
        for current_node, value in graph.items():
            if node != current_node:
                graph[current_node] = value - graph[node]
    return solve(graph)


def solve_part_one(seq):
    allergen_graph, ingredients = parse(seq)
    graph = solve(allergen_graph.copy())
    return sum(1 for ingredient in ingredients
               if ingredient not in graph.values())


def solve_part_two(seq):
    allergen_graph, _ = parse(seq)
    graph = solve(allergen_graph.copy())
    allergens = sorted(graph.keys())
    dangerous_ingredients = ','.join(graph[allergen] for allergen in allergens)
    return dangerous_ingredients


def main():
    input_seq = read_input('day21', 'input.txt')
    test_seq = read_input('day21', 'test.txt')

    assert solve_part_one(test_seq) == 5
    print('part one result: ', solve_part_one(input_seq))

    assert solve_part_two(test_seq) == 'mxmxvkd,sqjhc,fvjkl'
    print('part two result: ', solve_part_two(input_seq))


if __name__ == "__main__":
    main()

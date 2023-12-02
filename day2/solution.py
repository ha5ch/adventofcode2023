import re
import sys
from pathlib import Path


def get_data(file: str) -> list[str]:
    if Path(file).exists():
        with open(file) as f:
            return [l.strip() for l in f.readlines()]
    sys.exit(f'file "{file}" does not exist')


def part1_extract(dataset: str, config: dict[str, int]) -> int:
    game_nr = re.compile(r'^Game (\d+):')

    n = int(game_nr.findall(dataset)[0])
    # print(n)
    sets = dataset.split(': ')[1].split('; ')
    # print(sets)
    for set in sets:
        cubes = set.split(', ')
        # print(cubes)
        for cube in cubes:
            parts = re.findall(r'(\d+) (red|green|blue)', cube)
            # print(parts[0])
            count, color = parts[0]
            if config[color] < int(count):
                return 0

    return n


def part2_extract(dataset: list[str]) -> int:
    possibles = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    sets = dataset.split(': ')[1].split('; ')
    for set in sets:
        cubes = set.split(', ')
        for cube in cubes:
            parts = re.findall(r'(\d+) (red|green|blue)', cube)
            count, color = parts[0]
            if possibles[color] < int(count):
                possibles[color] = int(count)

    return possibles['red'] * possibles['green'] * possibles['blue']


def part1(data: list[str]):
    config = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }

    # print(data)
    # print(sum([validate(d, config) for d in data]))
    results = [part1_extract(d, config) for d in data]
    print(results, sum(results))


def part2(data: list[str]):
    results = [part2_extract(d) for d in data]
    print(results, sum(results))


if __name__ == '__main__':
    file = 'demo.txt'
    if len(sys.argv) == 2:
        file = sys.argv[1]

    data = get_data(file)

    print('-' * 10, 'part1', '-' * 10)
    part1(data)

    print('-' * 10, 'part2', '-' * 10)
    part2(data)

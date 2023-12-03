import sys
from pathlib import Path
import re

checks = [n for n in [(y, x) for y in range(-1, 2)
                      for x in range(-1, 2)] if n != (0, 0)]


def get_data(file: str) -> list[str]:
    if Path(file).exists():
        with open(file) as f:
            return [l.strip() for l in f.readlines()]
    sys.exit(f'file "{file}" does not exist')


def part1(data: list[str]):
    mod = len(data) + 1
    matrix = '.'.join(data)
    symbols_pattern = re.compile(r'[^\w\.]')
    idx = 0
    symbols = []
    while True:
        found = symbols_pattern.search(matrix, idx+1)
        if not found:
            break
        idx = found.start()
        symbols.append((idx // mod, idx % mod, idx))
        # print(symbols[-1], matrix[idx])

    # print("*" * 12)
    number_positions = set()
    for symbol in symbols:
        try:
            y, x, i = symbol
            for check in checks:
                _y, _x = check
                Y = y+_y
                X = x+_x
                if data[Y][X].isdecimal():
                    np = get_number_position(data, (Y, X))
                    # print(matrix[i], (Y, X), np, data[np[0]][np[1]:np[2]])
                    number_positions.add(np)
        except Exception as e:
            print(":(", e)
            raise e

    numbers = [int(data[y][s:e]) for (y, s, e) in number_positions]
    # print(numbers)
    print(sum(numbers))


def part2(data: list[str]):
    mod = len(data[0]) + 1
    matrix = '.'.join(data)
    gears = {}
    for i, c in enumerate(matrix):
        if c == '*':
            pg = (i // mod, i % mod, i)
            parts = set()
            for check in checks:
                y = pg[0] + check[0]
                x = pg[1] + check[1]
                if data[y][x].isdecimal():
                    parts.add(get_number_position(data, (y, x)))
            if len(parts) == 2:
                gears[pg] = product([int(data[y][s:e]) for (y, s, e) in parts])
    # print(gears)
    ratios = gears.values()
    # print(ratios)
    print(sum(ratios))


def get_number_position(data: list[str], core: tuple[int]) -> tuple[int]:
    y, x = core
    start = x
    end = x
    while start-1 >= 0 and data[y][start-1].isdecimal():
        start -= 1
    while end+1 < len(data[y]) and data[y][end+1].isdecimal():
        end += 1
    return (y, start, end+1)


def product(numbers) -> int:
    res = numbers[0]
    for n in numbers[1:]:
        res *= n
    return res


if __name__ == '__main__':
    file = 'demo.txt'
    if len(sys.argv) == 2:
        file = sys.argv[1]

    data = get_data(file)

    print('-' * 10, 'part1', '-' * 10)
    part1(data)

    print('-' * 10, 'part2', '-' * 10)
    part2(data)

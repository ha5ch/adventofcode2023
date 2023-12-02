import sys
from pathlib import Path


def get_data(file: str) -> list[str]:
    if Path(file).exists():
        with open(file) as f:
            return [l.strip() for l in f.readlines()]
    sys.exit(f'file "{file}" does not exist')


def part1(data: list[str]):
    ...


def part2(data: list[str]):
    ...


if __name__ == '__main__':
    file = 'demo.txt'
    if len(sys.argv) == 2:
        file = sys.argv[1]

    data = get_data(file)

    print('-' * 10, 'part1', '-' * 10)
    part1(data)

    print('-' * 10, 'part2', '-' * 10)
    part2(data)

import sys
from pathlib import Path


def get_data(file: str) -> list[str]:
    fp = Path(file)
    if fp.exists():
        with open(file) as f:
            return [l.strip() for l in f.readlines()]
    sys.exit(f'file "{file}" does not exist')


def extract_number(dataset: str) -> int:
    n = '0'
    for c in dataset:
        if c.isdigit():
            n = c
            break
    for c in dataset[::-1]:
        if c.isdigit():
            n += c
            break
    return int(n)


def part1(data: list[str]):
    numbers = [extract_number(d) for d in data]
    print(numbers, sum(numbers))


def part2(data: list[str]):
    converted = [convert(d) for d in data]
    part1(converted)


def convert(dataset: str) -> str:
    map = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
           'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    parts = []
    for i, c in enumerate(dataset):
        if c.isdigit():
            parts.append(c)
        elif len(dataset) - i >= 3:
            for k, v in map.items():
                if dataset[i:].startswith(k):
                    parts.append(v)
    return ''.join(parts)


if __name__ == '__main__':
    file = 'demo.txt'
    if len(sys.argv) == 2:
        file = sys.argv[1]

    data = get_data(file)

    print('-' * 10, 'part1', '-' * 10)
    part1(data)

    print('-' * 10, 'part2', '-' * 10)
    part2(data)

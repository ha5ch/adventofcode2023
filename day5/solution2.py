import sys
from pathlib import Path


def get_data(file: str) -> list[str]:
    if Path(file).exists():
        with open(file) as f:
            return [l.strip() for l in f.readlines()]
    sys.exit(f'file "{file}" does not exist')


def part1(data: list[str]):
    numbers = list(map(int, data[0].split(' ')[1:]))
    ranges = []
    for line in data[1:]:
        if line.strip() == '':
            continue
        if line.strip().endswith(':'):
            ranges.append([])
        else:
            ranges[-1].append(list(map(int, line.split(' '))))
    print(numbers)

    smallest = numbers[0]
    for n in numbers:
        print(n, end=" ")
        for rng in ranges:
            for r in rng:
                min = r[1]
                max = r[1] + r[2] - 1
                if min <= n <= max:
                    c = r[0] - r[1]
                    n += c
                    break
            print(n, end=" ")
        print()
        if n < smallest:
            smallest = n

    print(smallest)


def part2(data: list[str]):
    ... # TODO...


if __name__ == '__main__':
    file = 'demo.txt'
    if len(sys.argv) == 2:
        file = sys.argv[1]

    data = get_data(file)

    print('-' * 10, 'part1', '-' * 10)
    part1(data)

    print('-' * 10, 'part2', '-' * 10)
    part2(data)

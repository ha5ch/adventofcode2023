import sys
from pathlib import Path


def get_data(file: str) -> list[str]:
    if Path(file).exists():
        with open(file) as f:
            return [l.strip() for l in f.readlines()]
    sys.exit(f'file "{file}" does not exist')


def part1(data: list[str]):
    winning_numbers = [[int(n) for n in l.split(' | ')[0].split(
        ': ')[1].strip().split(' ') if n.isdecimal()] for l in data]
    my_numbers = [[int(n) for n in l.split(' | ')[1].strip().split(
        ' ') if n.isdecimal()] for l in data]
    # print(winning_numbers, my_numbers)

    points = [0] * len(winning_numbers)
    for card in range(len(winning_numbers)):
        for n in my_numbers[card]:
            if n in winning_numbers[card]:
                points[card] = points[card] * 2 if points[card] > 0 else 1
    print(points, sum(points))


def part2(data: list[str]):
    winning_numbers = [[int(n) for n in l.split(' | ')[0].split(
        ': ')[1].strip().split(' ') if n.isdecimal()] for l in data]
    my_numbers = [[int(n) for n in l.split(' | ')[1].strip().split(
        ' ') if n.isdecimal()] for l in data]

    cards = [0] * len(winning_numbers)
    for card in range(len(winning_numbers)):
        for n in my_numbers[card]:
            if n in winning_numbers[card]:
                cards[card] += 1
    # print(cards)
    copies = [1] * len(winning_numbers)
    for i, points in enumerate(cards):
            for j in range(i+1, points+i+1):
                copies[j] += copies[i]

    print(copies, sum(copies))


if __name__ == '__main__':
    file = 'demo.txt'
    if len(sys.argv) == 2:
        file = sys.argv[1]

    data = get_data(file)

    print('-' * 10, 'part1', '-' * 10)
    part1(data)

    print('-' * 10, 'part2', '-' * 10)
    part2(data)

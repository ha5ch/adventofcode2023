import sys
from pathlib import Path


def get_data(file: str) -> list[str]:
    if Path(file).exists():
        with open(file) as f:
            return [l.strip() for l in f.readlines()]
    sys.exit(f'file "{file}" does not exist')


def part1(data: list[str]):
    times = [int(x.strip()) for x in data[0].split(':')[1].strip().split()]
    distances = [int(x.strip()) for x in data[1].split(':')[1].strip().split()]
    print(times, distances)

    # distance = press * remaining
    result = 1
    for i, time in enumerate(times):
        wins = 0
        for press in range(1, time):
            distance = press * (time - press)
            if distance > distances[i]:
                wins += 1
        result *= wins if wins > 0 else 1
    print(result)


def part2(data: list[str]):
    time = int(''.join([x.strip()
               for x in data[0].split(':')[1].strip().split()]))
    distance = int(''.join([x.strip()
                   for x in data[1].split(':')[1].strip().split()]))
    print(time, distance)
    # wins = 0
    # for press in range(1, time//2):
    #     possible_distance = press * (time - press)
    #     if possible_distance > distance:
    #         wins += 1
    # print(wins*2+1)

    min = 0
    for press in range(time):
        if distance < press * (time - press):
            min = press
            break
    print(min, time-min*2 + 1)


if __name__ == '__main__':
    file = 'demo.txt'
    if len(sys.argv) == 2:
        file = sys.argv[1]

    data = get_data(file)

    print('-' * 10, 'part1', '-' * 10)
    part1(data)

    print('-' * 10, 'part2', '-' * 10)
    part2(data)

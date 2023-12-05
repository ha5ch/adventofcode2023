import sys
from pathlib import Path


def get_data(file: str) -> list[str]:
    if Path(file).exists():
        with open(file) as f:
            return [l.strip() for l in f.readlines()]
    sys.exit(f'file "{file}" does not exist')


def part1(data: list[str]):
    seeds = [int(x) for x in data[0].split(": ")[1].split(" ")]
    # print(seeds)
    maps = {}
    category = ""
    for i in range(2, len(data)):
        if len(data[i]) == 0:
            continue
        if data[i].endswith(":"):
            category = data[i].split(" ")[0]
            maps[category] = []
        else:
            maps[category].append([int(x) for x in data[i].split(" ")])

    """
    my first "naive" try to generate the ranges
    works fine with DEMO, but results in system crash because of memory problems (32GB RAM ;) )
    on my system :)
    """
    # print(maps)
    # def gen_range(dest, source, length):
    #     # print(dest, source, length)
    #     return {source+i: dest+i for i in range(length)}
    # range_maps = {
    #     key: merge_dicts([gen_range(*sub) for sub in val]) for key, val in maps.items()
    # }
    # print(range_maps['seed-to-soil'])
    # prev = seeds.copy()
    # for key in maps:
    #     converts = merge_dicts([gen_range(*sub) for sub in maps[key]])
    #     for i, source in enumerate(prev):
    #         dest = converts.get(source, source)
    #         prev[i] = dest
    #     print(prev)
    # print(prev, min(prev))

    results = seeds.copy()
    for key in maps:
        for i, val in enumerate(results):
            for dest, source, length in maps[key]:
                if source <= val <= source+length:
                    results[i] = (dest - source + val)
                    break
    print(results, min(results))



def merge_dicts(dicts):
    merged = {}
    for d in dicts:
        merged = {**merged, **d}
    return merged


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

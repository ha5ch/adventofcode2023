import sys
from pathlib import Path


def get_data(file: str) -> list[str]:
    if Path(file).exists():
        with open(file) as f:
            return [l.strip() for l in f.readlines()]
    sys.exit(f'file "{file}" does not exist')


def memory_guzzler(data: list[str]):
    """
    my first "naive" try to generate the ranges
    works fine with DEMO, but results in system crash because of memory problems (32GB RAM ;) )
    on my system :)
    """
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
    print(maps)

    def gen_range(dest, source, length):
        # print(dest, source, length)
        return {source+i: dest+i for i in range(length)}

    def merge_dicts(dicts):
        merged = {}
        for d in dicts:
            merged = {**merged, **d}
        return merged

    range_maps = {
        key: merge_dicts([gen_range(*sub) for sub in val]) for key, val in maps.items()
    }
    print(range_maps['seed-to-soil'])
    prev = seeds.copy()
    for key in maps:
        converts = merge_dicts([gen_range(*sub) for sub in maps[key]])
        for i, source in enumerate(prev):
            dest = converts.get(source, source)
            prev[i] = dest
        print(prev)
    print(prev, min(prev))


def part1(data: list[str]):
    seeds = [int(x) for x in data[0].split(": ")[1].split(" ")]
    print(seeds)
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

    results = seeds.copy()
    for rng in maps.values():
        for i, val in enumerate(results):
            for dest, source, length in rng:
                if source <= val <= source+length:
                    results[i] = (dest - source + val)
                    break
        print(results)
    print(results, min(results))


def part2(data: list[str]):
    seeds = [int(x) for x in data[0].split(": ")[1].split(" ")]
    print(seeds)

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


    # ???????

    # print(maps)
    
    # mins = set()
    # nums = []
    # smallest = seeds[0]

    # sts = maps['seed-to-soil']

    # for i in range(0, len(seeds), 2):
    #     n, m = seeds[i:i+2]
    #     print(n, m, list(range(n, n+m)), sts)
    #     for map in sts:
    #         if map[1] <= n <= map[1]+map[2]:
    #             n += map[0] + map[2]
    #     print(n, m)


    # for i in range(0, len(seeds), 2):
    #     #print(*seeds[i:i+2])
    #     n, m = seeds[i:i+2]
    #     for j, val in enumerate(range(n, n+m)):
    #         # nums.append(val)
    #         for name, rng in maps.items():
    #             print(name, rng)
    #             s = sorted(rng, key=lambda x: x[1])
    #             min_source = s[0][1]
    #             max_source = s[-1][1] + s[-1][2]
    #             if not (min_source <= val <= max_source):
    #                 continue
    #             for dest, source, length in rng:
    #                 if source <= val <= source+length:
    #                     val = (dest - source + val)
    #                     break
    #         #print(smallest, val, "\n")
    #         if val < smallest:
    #             smallest = val
    #     print(smallest)

    # print(smallest)
    # mins = sorted(set(mins))
    # print(sorted(nums))
    # print(mins, min(mins))

if __name__ == '__main__':
    file = 'demo.txt'
    if len(sys.argv) == 2:
        file = sys.argv[1]

    data = get_data(file)

    print('-' * 10, 'part1', '-' * 10)
    part1(data)

    print('-' * 10, 'part2', '-' * 10)
    part2(data)

from typing import List

def create_range(value: str) -> List[int]:
    [start, stop] = value.split('-')
    return range(int(start), int(stop) + 1)

with open('day-3/input.txt', 'r') as source:
    count = 0
    lines = source.read().splitlines()
    for line in lines:
        [first, second] = line.split(',')

        first_range = set(create_range(first))
        second_range = set(create_range(second))

        if first_range & second_range:
            count = count + 1

    print(count)

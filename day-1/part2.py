from itertools import groupby
from typing import List

def elf_value(elf: List[str]) -> int:
    return sum([int(v) for v in elf])

with open('day-1/part2-input.txt', 'r') as source:
    lines = source.read().splitlines()
    raw_elf_values = [list(y) for x, y in groupby(lines, lambda value: value == "") if not x]
    elf_values = [elf_value(elf) for elf in raw_elf_values]
    elf_values.sort()
    elf_values.reverse()
    print(sum(elf_values[0:3]))

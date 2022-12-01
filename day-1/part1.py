from itertools import groupby
from typing import List

def elf_value(elf: List[str]) -> int:
    return sum([int(v) for v in elf])

with open('day-1/part1-input.txt', 'r') as source:
    lines = source.read().splitlines()
    raw_elf_values = [list(y) for x, y in groupby(lines, lambda value: value == "") if not x]
    elf_values = [elf_value(elf) for elf in raw_elf_values]
    print(max(elf_values))

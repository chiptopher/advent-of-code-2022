from typing import List, Dict
from collections import defaultdict

CRATES_END = 8
#CRATES_END = 3

def generate_crates(source: List[str]) -> Dict[int, List[str]]:
    chunks_list = []
    for line in source:

        def process_string(raw):
            return raw.replace('[', '').replace(']', '').strip()

        chunks_list.append([process_string(line[i:i+4]) for i in range(0, len(line), 4)])

    crates = defaultdict(lambda: [])

    for row in reversed(chunks_list):
        for (index, crate_maybe) in enumerate(row):
            if crate_maybe != '':
                crates[index + 1].append(crate_maybe)

    return crates

def generate_actions(lines):
    result = []
    for line in lines:
        split = line.split(' ')
        result.append((split[1], split[3], split[5]))
    return result


with open('day-5/input.txt', 'r') as source:
    lines = source.read().splitlines()
    crates = generate_crates(lines[:CRATES_END])

    actions = generate_actions(lines[CRATES_END + 2:])
    for action in actions:
        (count, from_crate, to) = action
        for i in range(int(count)):
            if crates[int(from_crate)]:
                value = crates[int(from_crate)].pop()
                crates[int(to)].append(value)
    result = ''
    for c in sorted(crates):
        result = result + crates[c].pop()

    print(result)

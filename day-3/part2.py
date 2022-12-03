
from string import ascii_lowercase, ascii_uppercase

with open('day-3/input.txt', 'r') as source:
    lines = source.read().splitlines()
    score = 0
    key = {}
    for (index, letter) in enumerate(ascii_lowercase):
        key[letter] = index + 1
    for (index, letter) in enumerate(ascii_uppercase):
        key[letter] = index + 27
    for index in range(0, len(lines), 3):
        [line1, line2, line3] = lines[index:index+3]

        common = set(line1).intersection(set(line2)).intersection(set(line3))
        char = list(common)[0]
        score = score + key[char]
    print(score)

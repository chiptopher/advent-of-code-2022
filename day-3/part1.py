from string import ascii_lowercase, ascii_uppercase

with open('day-3/input.txt', 'r') as source:
    score = 0
    key = {}
    for (index, letter) in enumerate(ascii_lowercase):
        key[letter] = index + 1
    for (index, letter) in enumerate(ascii_uppercase):
        key[letter] = index + 27
    for line in source:
        left = line[:int(len(line) / 2)]
        right = line[int(len(line) / 2):]

        common = set(left).intersection(set(right))
        char = list(common)[0]

        score = score + key[char]
    print(score)

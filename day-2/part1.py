class Option:
    def __init__(self, symbols, value):
        self.beats = None
        self.symbols = symbols
        self.value = value

    def score(self, other):
        if other == self:
            return self.value + 3
        if self.beats == other:
            return self.value + 6
        if other.beats == self:
            return self.value

    def find(self, symbol):
        return symbol in self.symbols

with open('day-2/part1-input.txt', 'r') as source:

    rock = Option({'A', 'X'}, 1)
    paper = Option({'B', 'Y'}, 2)
    scissors = Option({'C', 'Z'}, 3)

    rock.beats = scissors
    paper.beats = rock
    scissors.beats = paper

    score = 0

    for line in source.read().splitlines():
        [theirs, mine] = line.split()

        their_symbol = next(x for x in [rock, paper, scissors] if x.find(theirs))
        my_symbol = next(x for x in [rock, paper, scissors] if x.find(mine))
        score = score + my_symbol.score(their_symbol)

    print(score)

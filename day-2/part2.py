class Option:
    def __init__(self, symbols, value):
        self.beats = None
        self.beaten_by = None
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

    rock = Option({'A'}, 1)
    paper = Option({'B'}, 2)
    scissors = Option({'C'}, 3)

    rock.beats = scissors
    rock.beaten_by = paper

    paper.beats = rock
    paper.beaten_by = scissors

    scissors.beats = paper
    scissors.beaten_by = rock

    score = 0

    for line in source.read().splitlines():
        [theirs, condition] = line.split()

        their_symbol = next(x for x in [rock, paper, scissors] if x.find(theirs))
        my_symbol = None

        if condition == 'X':
            my_symbol = their_symbol.beats
        elif condition == 'Z':
            my_symbol = their_symbol.beaten_by
        else:
            my_symbol = their_symbol

        score = score + my_symbol.score(their_symbol)

    print(score)

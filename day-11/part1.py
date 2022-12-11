from typing import List

class Monkey:
    def __init__(self, id, starting_items, operation, divisor, true, false):
        self.id = id
        self.items = starting_items
        self.operation = operation
        self.divisor = divisor
        self.true = true
        self.false = false
        self.inspection_count = 0

def _parse_monkey(index, lines):
    starting_items = [int(i) for i in lines[1].replace('  Starting items: ', '').split(', ')]
    line2 = lines[2].replace('Operation: new = old ', '')
    operation = None

    if '+' in line2:
        value = line2.replace('+', '').strip()
        if value == 'old':
            operation = lambda x: x + x
        else:
            operation = lambda x: x + int(value)

    if '*' in line2:
        value = line2.replace('*', '').strip()
        if value == 'old':
            operation = lambda x: x * x
        else:
            operation = lambda x: x * int(value)

    divisor = int(lines[3].replace('  Test: divisible by', ''))
    true = int(lines[4].replace('    If true: throw to monkey ', ''))
    false = int(lines[5].replace('    If false: throw to monkey ', ''))

    monkey = Monkey(index, starting_items, operation, divisor, true, false)
    return monkey


if __name__ == '__main__':
    with open('day-11/input.txt', 'r') as source:
        lines = source.read().splitlines()
        monkeys = []
        for i in range(0, len(lines), 7):
            monkeys.append(_parse_monkey(len(monkeys), lines[i:i+6]))

        for i in range(20):
            for monkey in monkeys:
                while len(monkey.items) > 0:
                    new_item = monkey.items[0]
                    monkey.items = monkey.items[1:]
                    new_level = monkey.operation(new_item)
                    monkey.inspection_count += 1
                    new_level = int(new_level / 3)
                    to_monkey = None
                    if new_level % monkey.divisor == 0:
                        to_monkey = monkey.true
                    else:
                        to_monkey = monkey.false
                    to_monkey = next(monkey for monkey in monkeys if monkey.id == to_monkey)
                    to_monkey.items.append(new_level)
                
        monkey_business = list(reversed(sorted(monkey.inspection_count for monkey in monkeys)))[0:2]
        print(f'Monkey business: {monkey_business[0] * monkey_business[1]}')





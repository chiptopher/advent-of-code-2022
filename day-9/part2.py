class Node:
    def __init__(self, tail = None, name = ''):
        self.name = name
        self.current_position = (0,0)
        self.visited = set(self.current_position)
        self.tail = tail

    def take_step(self, direction):
        (y, x) = self.current_position
        if direction == 'U':
            y -= 1
        if direction == 'D':
            y += 1
        if direction == 'R':
            x += 1
        if direction == 'L':
            x -= 1
        self.current_position = (y, x)

class Tail(Node):
    def move(self, head):
        (self_y, self_x) = self.current_position
        (head_y, head_x) = head.current_position

        y_diff = head_y - self_y
        x_diff = head_x - self_x

        if abs(y_diff) <= 1 and abs(x_diff) <= 1:
            return

        if y_diff > 1:
            self.take_step('D')
            if x_diff > 0:
                self.take_step('R')
            if x_diff < 0:
                self.take_step('L')

        elif y_diff < -1:
            self.take_step('U')
            if x_diff > 0:
                self.take_step('R')
            if x_diff < 0:
                self.take_step('L')

        elif x_diff > 1:
            self.take_step('R')
            if y_diff > 0:
                self.take_step('D')
            if y_diff < 0:
                self.take_step('U')

        elif x_diff < -1:
            self.take_step('L')
            if y_diff > 0:
                self.take_step('D')
            if y_diff < 0:
                self.take_step('U')

        self.visited.add(self.current_position)
        if self.tail:
            self.tail.move(self)


class Head(Node):
    def move(self, direction):
        self.take_step(direction)
        self.visited.add(self.current_position)
        self.tail.move(self)


if __name__ == '__main__':
    with open('day-9/input.txt', 'r') as source:
        lines = source.read().splitlines()
        nine = Tail(None, '9')
        eight = Tail(nine, '8')
        seven = Tail(eight, '7')
        six = Tail(seven, '6')
        five = Tail(six, '5')
        four = Tail(five, '4')
        three = Tail(four, '3')
        two = Tail(three, '2')
        one = Tail(two, '1')
        head = Head(one, '0')

        for line in lines:
            [direction, amount] = line.split(' ')
            for _ in range(int(amount)):
                head.move(direction)
                #print(head.current_position, one.current_position)
        print('Part 1: ' + str(len(one.visited)))
        print('Part 2: ' + str(len(nine.visited)))



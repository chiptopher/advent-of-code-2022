class Tail:
    def __init__(self):
        self.visited = set()
        self.current_position = (0,0)

    def move(self, head):
        (self_y, self_x) = self.current_position
        (head_y, head_x) = head.current_position
        if abs(head_y - self_y) > 1 or abs(head_x - self_x) > 1:
            self.current_position = head.previous_position
            self.visited.add(self.current_position)


class Head:
    def __init__(self):
        self.current_position = (0,0)
        self.previous_position = None
        self.tail = Tail()

    def move(self, direction):
        self.previous_position = self.current_position
        (y, x) = self.current_position

        if direction == 'U':
            y -= 1
        if direction == 'D':
            y +=1
        if direction == 'R':
            x += 1
        if direction == 'L':
            x -= 1
        self.current_position = (y, x)
        self.tail.move(self)


with open('day-9/input.txt', 'r') as source:
    lines = source.read().splitlines()
    head = Head()
    for line in lines:
        [direction, amount] = line.split(' ')
        for _ in range(int(amount)):
            head.move(direction)
    print(len(head.tail.visited))



from typing import List, Tuple


class Spot:
    def __init__(self, y, x, height):
        self.x = x
        self.y = y
        self.height = height
        self.visited = False

    def __str__(self):
        return f"({self.y}, {self.x}) | {self.height} | {self.visited}"

    def traverse(self, topography) -> Tuple[int, bool]:
        self.visited = True

        if self.height == 'E':
            return (1, True)

        up = self.get_up()
        down = self.get_down()
        left = self.get_left()
        right = self.get_right()

        if any(path for path in [up, down, left, right]):
            for path in filter(lambda path: path != None, [up, down, left, right]):

        else:
            return [1, False]

    def get_up(self, topography) -> 'Spot':
        point = (self.y - 1, self.x)
        if _point_out_of_bounds(point, topography):
            pass
        else:
            return topography[point]

    def get_down(self) -> 'Spot':
        pass

    def get_left(self) -> 'Spot':
        pass

    def get_right(self) -> 'Spot':
        pass

    def _point_out_of_bounds(self, point, topography) -> bool:
        y = next(reversed(sorted([p[0] for p in list(topography)])))
        x = next(reversed(sorted([p[1] for p in list(topography)])))

        (py, px) = point

        return (
            py < 0 or
            px < 0 or
            py > y or
            px > x
        )

if __name__ == '__main__':
    with open('day-12/input.txt', 'r') as source:
        topography = {}
        lines = source.read().splitlines()
        for (y, line) in enumerate(lines):
            for (x, height) in enumerate([*line]):
                topography[(y, x)] = Spot(y, x, height)

        start = topography[(0, 0)]
        print(start)



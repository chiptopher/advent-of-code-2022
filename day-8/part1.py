from typing import Tuple

class Tree:
    def __init__(self, forrest, coords: Tuple[int, int], height: int):
        self.forrest = forrest
        self.coords = coords
        self.height = height

    def highest_in_direction(self, direction: str) -> int:
        neighbor_highest = self.neightbor_highest(direction)
        return neighbor_highest if neighbor_highest > self.height else self.height

    def neightbor_highest(self, direction: str) -> int:
        if self._is_on_edge():
            return self.height
        return self._get_neightbor(direction).highest_in_direction(direction)

    def _is_on_edge(self) -> bool:
        (y, x) = self.coords
        return x == 0 or y == 0 or x >= (forest_width - 1) or y >= (forest_height - 1)
    

    def is_visible(self) -> bool:
        if self._is_on_edge():
            return True
        visible = (
            self.neightbor_highest('left') < self.height or
            self.neightbor_highest('right') < self.height or
            self.neightbor_highest('up') < self.height or
            self.neightbor_highest('down') < self.height
        )
        return visible

    def _get_neightbor(self, direction) -> 'Tree':
        (y, x) = self.coords
        if direction == 'up':
            y -= 1
        if direction ==  'down':
            y +=1
        if direction ==  'right':
            x += 1
        if direction ==  'left':
            x -= 1
        return self.forrest[(y, x)]



with open('day-8/input.txt', 'r') as source:
    forrest = dict()
    lines = source.read().splitlines()

    global forest_width
    forest_width = len(lines[0])

    global forest_height
    forest_height = len(lines)

    for (row_index, line) in enumerate(lines):
        for (coulmn_index, height) in enumerate(line):
            coords = (row_index, coulmn_index)
            forrest[coords] = Tree(forrest, coords, int(height))

    visible_count = 0
    for key in list(forrest):
        tree = forrest[key]
        if tree.is_visible():
            visible_count += 1

    print(visible_count)

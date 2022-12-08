from typing import Tuple

class Tree:
    def __init__(self, forrest, coords: Tuple[int, int], height: int):
        self.forrest = forrest
        self.coords = coords
        self.height = height

    def _is_on_edge(self) -> bool:
        (y, x) = self.coords
        return x == 0 or y == 0 or x >= (forest_width - 1) or y >= (forest_height - 1)

    def neightbor_scenic(self, direction, from_height) -> int:
        if self._is_on_edge():
            return 0
        neighbor = self._get_neightbor(direction)
        if neighbor.height >= from_height:
            return 1
        else:
            return neighbor.neightbor_scenic(direction, from_height) + 1

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

    def scenic_score(self) -> int:
        return (
            tree.neightbor_scenic('up', self.height) *
            tree.neightbor_scenic('down', self.height) *
            tree.neightbor_scenic('left', self.height) *
            tree.neightbor_scenic('right', self.height)
        )



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

    scores = []
    for key in list(forrest):
        tree = forrest[key]
        scores.append(tree.scenic_score())

    print(max(scores))

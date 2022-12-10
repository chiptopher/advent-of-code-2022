import unittest

from part2 import Node, Tail, Head

class TestNode_take_step(unittest.TestCase):

    def test_works(self):
        cases = [
            ('U', (-1, 0)),
            ('D', (1, 0)),
            ('L', (0, -1)),
            ('R', (0, 1)),
        ]
        for test_case in cases:
            [direction, point] = test_case
            node = Node(None)
            node.take_step(direction)
            [y, x] = node.current_position
            [expected_y, expected_x] = point
            self.assertEqual(expected_y, y, f'Expected y {expected_y} but got {y} for {direction}')
            self.assertEqual(expected_x, x, f'Expected x {expected_x} but got {x} for {direction}')


class Tail_move(unittest.TestCase):
    def test_inline_cases(self):
        cases = [
            ('U', (-2, 0), (-1, 0)),
            ('D', (2, 0), (1, 0)),
            ('L', (0, -2), (0, -1)),
            ('R', (0, 2), (0, 1)),
        ]

        for (index, test_case) in enumerate(cases):
            [direction, head_position, expected_tail_position] = test_case
            tail = Tail(None)
            head = Tail(tail)

            head.current_position = head_position
            tail.current_position = (0, 0)

            tail.move(head)

            self.assertEqual(expected_tail_position, tail.current_position, f"  for  {index}")

    def test_diagnal_moves(self):
        cases = [
            ((-2, 1), (-1, 1)),   # up right
            ((2, 1), (1, 1)),     # down right
            ((-2, -1), (-1, -1)), # up left
            ((2, -1), (1, -1)),   # down left
            ((-1, -2), (-1, -1)), # left up 
            ((-1, 2), (-1, 1)),   # right up
            ((1, -2), (1, -1)),   # left down
            ((1, 2), (1, 1)),     # right down
        ]
        for (index, test_case) in enumerate(cases):
            [head_position, expected_tail_position] = test_case
            tail = Tail(None)
            head = Tail(tail)
            head.current_position = head_position
            tail.current_position = (0, 0)
            tail.move(head)

            self.assertEqual(expected_tail_position, tail.current_position, f"  for  {index}")


class Test_main(unittest.TestCase):
    def test_part1(self):
        one = Tail(None)
        head = Head(one)

        head.move('R')
        head.move('R')
        head.move('R')
        head.move('R')
        self.assertEqual((0, 3), one.current_position)
        self.assertEqual(4, len(one.visited))

        head.move('U')
        head.move('U')
        head.move('U')
        head.move('U')
        self.assertEqual((-3, 4), one.current_position)
        self.assertEqual(7, len(one.visited))

        head.move('L')
        head.move('L')
        head.move('L')
        self.assertEqual((-4, 2), one.current_position)

        head.move('D')
        self.assertEqual((-4, 2), one.current_position)

        head.move('R')
        self.assertEqual((-4, 2), one.current_position)

        head.move('R')
        self.assertEqual((-4, 2), one.current_position)

        head.move('R')
        self.assertEqual((-3, 3), one.current_position)

        head.move('R')
        self.assertEqual((-3, 4), one.current_position)
        self.assertEqual((-3, 5), head.current_position)

        head.move('D')
        self.assertEqual((-3, 4), one.current_position)
        self.assertEqual((-2, 5), head.current_position)

        head.move('L')
        head.move('L')
        head.move('L')
        self.assertEqual((-2, 3), one.current_position)

        head.move('L')
        head.move('L')

        head.move('R')
        head.move('R')

        self.assertEqual((-2, 1), one.current_position)
        self.assertEqual(13, len(one.visited))


    def test_part2_small(self):
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

        head.move('R')
        head.move('R')
        head.move('R')
        head.move('R')

        self.assertEqual((0, 0), four.current_position)

        head.move('U')
        head.move('U')
        self.assertEqual((-1, 4), one.current_position)
        self.assertEqual((-1, 3), two.current_position)
        self.assertEqual((-1, 2), three.current_position)
        self.assertEqual((-1, 1), four.current_position)
        head.move('U')
        self.assertEqual((-2, 4), one.current_position)
        self.assertEqual((-1, 3), two.current_position)
        self.assertEqual((-1, 2), three.current_position)
        self.assertEqual((-1, 1), four.current_position)
        self.assertEqual((0, 0), five.current_position)
        head.move('U')
        self.assertEqual((-3, 4), one.current_position)
        self.assertEqual((-2, 4), two.current_position)
        self.assertEqual((-2, 3), three.current_position)
        self.assertEqual((-2, 2), four.current_position)
        self.assertEqual((-1, 1), five.current_position)
        self.assertEqual((0, 0), six.current_position)

        head.move('L')
        head.move('L')
        head.move('L')

        head.move('D')

        head.move('R')
        head.move('R')
        head.move('R')
        head.move('R')

        head.move('D')

        head.move('L')
        head.move('L')
        head.move('L')
        head.move('L')
        head.move('L')

        head.move('R')
        head.move('R')

        self.assertEqual((-2, 2), head.current_position)
        self.assertEqual((-1, 1), five.current_position)
        self.assertEqual((0, 0), nine.current_position)

    """
    def test_part2_big(self):
        nine = Tail(None)
        eight = Tail(nine)
        seven = Tail(eight)
        six = Tail(seven)
        five = Tail(six)
        four = Tail(five)
        three = Tail(four)
        two = Tail(three)
        one = Tail(two)
        head = Head(one)

        def move(direction, count):
            for _ in range(count):
                head.move(direction)

        move('R', 5)
        move('U', 8)
        self.assertEqual(1, len(nine.visited))
        head.move('L')
        head.move('L')
        head.move('L')
        head.move('L')

        head.move('L')
        self.assertEqual((-1, 1), nine.current_position)
        self.assertEqual(1, len(nine.visited))

        head.move('L')
        head.move('L')
        head.move('L')
        self.assertEqual(3, len(nine.visited))
        move('D', 3)
        move('R', 17)
        move('D', 10)
        move('L', 25)
        move('U', 20)

        self.assertEqual((-15, -11), head.current_position)
        self.assertEqual((-6, -11), nine.current_position)
        self.assertEqual(36, len(nine.visited))
    """


if __name__ == '__main__':
    unittest.main()

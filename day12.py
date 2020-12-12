from utils import read_input


class Ship():
    def __init__(self, x=0, y=0, direction=0):
        self.x = x
        self.y = y
        self.direction = direction

    def action(self, order):
        opeartion = order[:1]
        value = int(order[1:])

        if opeartion == 'N':
            self.y += value

        if opeartion == 'S':
            self.y -= value

        if opeartion == 'E':
            self.x += value

        if opeartion == 'W':
            self.x -= value

        if opeartion == 'F':
            x1, y1 = self._trans_direction()
            self.x += x1 * value
            self.y += y1 * value

        if opeartion == 'R':
            self.direction -= value
            self._clear_direction()

        if opeartion == 'L':
            self.direction += value
            self._clear_direction()

    def _clear_direction(self):
        if (self.direction < 0) or (self.direction >= 360):
            self.direction -= (self.direction // 360) * 360

    def _trans_direction(self):
        if self.direction == 0:
            return 1, 0
        if self.direction == 90:
            return 0, 1
        if self.direction == 180:
            return -1, 0
        if self.direction == 270:
            return 0, -1


class Ship_waypoint(Ship):
    def __init__(self, x=0, y=0, x1=10, y1=1,  direction=0):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.direction = direction

    def action(self, order):
        operation = order[:1]
        value = int(order[1:])

        if operation == 'N':
            self.y1 += value
        if operation == 'S':
            self.y1 -= value
        if operation == 'E':
            self.x1 += value
        if operation == 'W':
            self.x1 -= value
        if operation == 'F':
            self.x += value * (self.x1)
            self.y += value * (self.y1)
        if operation == 'R':
            self.direction -= value
            self._clear_direction()
            self._trans_direction()
        if operation == 'L':
            self.direction += value
            self._clear_direction()
            self._trans_direction()

    def _trans_direction(self):
        if self.direction == 0:
            pass
        if self.direction == 90:
            self.x1, self.y1 = -self.y1, self.x1
        if self.direction == 180:
            self.x1, self.y1 = -self.x1, -self.y1
        if self.direction == 270:
            self.x1, self.y1 = self.y1, -self.x1
        self.direction = 0


def solve_part_one(seq):
    ship = Ship()
    for each in seq:
        ship.action(each.strip())
    return abs(ship.x) + abs(ship.y)


def solve_part_two(seq):
    ship = Ship_waypoint()
    for each in seq:
        ship.action(each.strip())
    return abs(ship.x) + abs(ship.y)


def main():
    input_seq = read_input('day12', 'input.txt')
    test_seq = read_input('day12', 'test.txt')

    assert solve_part_one(test_seq) == 25
    print('part one result: ', solve_part_one(input_seq))

    assert solve_part_two(test_seq) == 286
    print('part two result: ', solve_part_two(input_seq))


if __name__ == "__main__":
    main()

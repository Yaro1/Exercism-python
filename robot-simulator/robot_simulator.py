# Globals for the directions
# Change the values as you see fit

NORTH = (lambda x: (x[0], x[1] + 1))
SOUTH = (lambda x: (x[0], x[1] - 1))
EAST = (lambda x: (x[0] + 1, x[1]))
WEST = (lambda x: (x[0] - 1, x[1]))


class Robot:
    direct = {0: NORTH, 1: EAST, 2: SOUTH, 3: WEST}

    def __init__(self, direction=NORTH, x=0, y=0):
        self.number_dir = list(Robot.direct.values()).index(direction)
        self.direction = direction
        self.coordinates = x, y

    def move(self, str_):
        for i in str_:
            if i == "A":
                self.coordinates = self.direction(self.coordinates)
            else:
                self.number_dir = (self.number_dir + 3) % 4 if i == "L" else (self.number_dir + 1) % 4
                self.direction = Robot.direct[self.number_dir]

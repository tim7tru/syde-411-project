from point import *

# FAR - Floor area ratio
MIN_FAR = 0.10
MAX_FAR = 0.20


DIRECTIONS = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
    (1, 1),
    (1, -1),
    (-1, -1),
    (-1, 1)
]


def generate_walls(length, width):
    total_area = length * width
    far = rand.uniform(MIN_FAR, MAX_FAR)
    wall_area = far * total_area

    walls = set()

    while len(walls) < wall_area:
        x, y = generate_random_point(length, width)
        dir_x, dir_y = DIRECTIONS[int(rand.uniform(1, len(DIRECTIONS)))]
        wall_length = rand.uniform(1, min(length, width))
        curr_length = 0

        while length > x >= 0 and width > y >= 0 and curr_length < wall_length:
            walls.add((x, y))
            x += dir_x
            y += dir_y
            curr_length += 1

    return walls

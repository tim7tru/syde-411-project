import random as rand
import numpy as np


def generate_random_point(max_x, max_y):
    x = rand.randint(0, max_x - 1)
    y = rand.randint(0, max_y - 1)
    return x, y


def generate_access_points(n: int, max_length: int, max_width: int, walls):
    if n > max_width * max_length:
        return

    access_points = []

    while len(access_points) < n:
        point = generate_random_point(max_length, max_width)
        if point not in access_points and point not in walls:
            access_points.append(point)

    return np.array(access_points)

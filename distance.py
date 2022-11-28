from enum import Enum
import random as rand


class DistanceType(Enum):
    CHEBYSHEV = 1
    CUSTOM = 2


def chebyshev_dist(a: (int, int), b: (int, int)):
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    return max(dx, dy)


def custom_dist(a: (int, int), b: (int, int), walls):
    cheb = chebyshev_dist(a, b)

    dx = (b[0] - a[0]) / cheb
    dy = (b[1] - a[1]) / cheb

    curr = a
    dist = 0

    while round(curr[0]) != b[0] or round(curr[1]) != b[1]:
        new_point = (curr[0] + dx, curr[1] + dy)

        # Add wall weight in here
        dist += 1  # + weight if new_point is wall
        if new_point in walls:
            dist *= (1 + rand.uniform(0.25, 1.25))
        curr = new_point

    return dist
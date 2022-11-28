from point import *
from distance import *


THRESHOLD = 0.000000001


def weiszfeld(access_points, walls, length, width, distance_type):
    prev = generate_random_point(length, width)
    prev_dist = 0

    while True:
        dist = []

        for point in access_points:
            if distance_type == DistanceType.CHEBYSHEV:
                dist.append(chebyshev_dist(prev, point))
            elif distance_type == DistanceType.CUSTOM:
                dist.append(custom_dist(prev, point, walls))

        np_dist = np.array([dist, ] * 2).transpose()
        num = (access_points / np_dist).sum(axis=0)
        denom = (np.ones((len(access_points), 2)) / np_dist).sum(axis=0)
        new_point = num / denom
        curr_dist = np_dist.mean()
        prev = (new_point[0], new_point[1])
        if has_met_threshold(prev_dist, curr_dist):
            break

        prev_dist = curr_dist

    print(f"Distance: {prev_dist}")
    return round(prev[0]), round(prev[1])


def has_met_threshold(prev, curr):
    num = abs(prev - curr)
    denom = (prev + curr) / 2
    return (num / denom) <= THRESHOLD

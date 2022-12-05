from point import *
from distance import *

THRESHOLD = 0.000000001


def centroid(access_points):
    n = len(access_points)
    sum_x = 0
    sum_y = 0
    for pt in access_points:
        sum_x += pt[0]
        sum_y += pt[1]

    return sum_x / n, sum_y / n


def weiszfeld(access_points, walls):
    prev = centroid(access_points)
    prev_dist = 0

    while True:
        dist = []

        for point in access_points:
            dist.append(custom_dist(prev, point, walls))

        np_dist = np.array([dist, ] * 2).transpose()
        num = (access_points / np_dist).sum(axis=0)
        denom = (np.ones((len(access_points), 2)) / np_dist).sum(axis=0)
        new_point = num / denom
        curr_dist = np_dist.mean()
        prev = new_point
        if has_met_threshold(prev_dist, curr_dist):
            break

        prev_dist = curr_dist

    print(f"Final Pt: {prev}")
    print(f"Distance: {prev_dist}")
    return round(prev[0]), round(prev[1])


def has_met_threshold(prev, curr):
    num = abs(prev - curr)
    denom = (prev + curr) / 2
    return (num / denom) <= THRESHOLD

from weiszfeld import *
from plot import *
from wall import *
from sklearn.cluster import KMeans

import time as time
import numpy as np

LENGTH = 50
WIDTH = 50
NUM_ACCESS_POINTS = 20


def one_router(walls, ap):
    return weiszfeld(ap, walls)


def two_routers(walls, ap):
    kmeans = KMeans(n_clusters=2, random_state=0)
    kmeans.fit(ap)

    first_cluster = ap[kmeans.labels_ == 0]
    second_cluster = ap[kmeans.labels_ == 1]

    x1, y1 = weiszfeld(first_cluster, walls)
    x2, y2 = weiszfeld(second_cluster, walls)

    return (x1, y1), (x2, y2)


def three_routers(walls, ap):
    kmeans = KMeans(n_clusters=3, random_state=0)
    kmeans.fit(ap)

    first_cluster = ap[kmeans.labels_ == 0]
    second_cluster = ap[kmeans.labels_ == 1]
    third_cluster = ap[kmeans.labels_ == 2]

    x1, y1 = weiszfeld(first_cluster, walls)
    x2, y2 = weiszfeld(second_cluster, walls)
    x3, y3 = weiszfeld(third_cluster, walls)

    return (x1, y1), (x2, y2), (x2, y3)


if __name__ == "__main__":
    walls = generate_walls(LENGTH, WIDTH)
    ap = generate_access_points(NUM_ACCESS_POINTS, LENGTH, WIDTH, walls)
    end_times = []

    one_start = time.time()
    one = one_router(walls, ap)
    end_times.append(time.time())

    two_start = time.time()
    two = two_routers(walls, ap)
    end_times.append(time.time())

    three_start = time.time()
    three = three_routers(walls, ap)
    end_times.append(time.time())

    arr1 = np.zeros((LENGTH, WIDTH))
    arr2 = np.zeros((LENGTH, WIDTH))
    arr3 = np.zeros((LENGTH, WIDTH))

    for pt in ap:
        arr1[pt[0]][pt[1]] = 3
        arr2[pt[0]][pt[1]] = 3
        arr3[pt[0]][pt[1]] = 3

    for pt in walls:
        arr1[pt[0]][pt[1]] = 4
        arr2[pt[0]][pt[1]] = 4
        arr3[pt[0]][pt[1]] = 4

    arr1[one[0]][one[1]] = 2

    for pt in two:
        arr2[pt[0]][pt[1]] = 2

    for pt in three:
        arr3[pt[0]][pt[1]] = 2

    plot_grid(arr1)
    plot_grid(arr2)
    plot_grid(arr3)

    # print(f"Custom end time: {custom_end - start}")
    print(f"One router duration: {end_times[0] - one_start}")
    print(f"Two router duration: {end_times[1] - two_start}")
    print(f"Three router duration: {end_times[2] - three_start}")


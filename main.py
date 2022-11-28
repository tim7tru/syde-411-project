from weiszfeld import *
from plot import *
from wall import *
from sklearn.cluster import KMeans

import time as time
import numpy as np

if __name__ == "__main__":
    start = time.time()
    LENGTH = 1000
    WIDTH = 1000
    NUM_ACCESS_POINTS = 100

    walls = generate_walls(LENGTH, WIDTH)
    ap = generate_access_points(NUM_ACCESS_POINTS, LENGTH, WIDTH, walls)
    kmeans = KMeans(n_clusters=3, random_state=0)
    kmeans.fit(ap)

    first_cluster = ap[kmeans.labels_ == 0]
    second_cluster = ap[kmeans.labels_ == 1]
    third_cluster = ap[kmeans.labels_ == 2]

    x1, y1 = weiszfeld(first_cluster, walls, LENGTH, WIDTH, DistanceType.CUSTOM)
    x2, y2 = weiszfeld(second_cluster, walls, LENGTH, WIDTH, DistanceType.CUSTOM)
    x3, y3 = weiszfeld(third_cluster, walls, LENGTH, WIDTH, DistanceType.CUSTOM)

    custom_end = time.time()
    arr = np.zeros((LENGTH, WIDTH))

    for pt in ap:
        arr[pt[0]][pt[1]] = 3

    for pt in walls:
        arr[pt[0]][pt[1]] = 4

    arr[x1][y1] = 2
    arr[x2][y2] = 2
    arr[x3][y3] = 2

    plot_grid(arr)

    print(f"Custom end time: {custom_end - start}")
    print(f"Program end time: {time.time() - start}")

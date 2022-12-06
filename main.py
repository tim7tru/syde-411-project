from weiszfeld import *
from plot import *
from wall import *
from sklearn.cluster import KMeans

import time as time
import numpy as np

# Add wall and AP coords here
HAS_WALLS = False
WALLS = []
ACCESS_POINTS = []
LENGTH = -1
WIDTH = -1
ROUTERS = -1


def n_routers(n, walls, ap):
    kmeans = KMeans(n_clusters=n, random_state=0)
    kmeans.fit(ap)
    coords = []
    for i in range(n):
        cluster = ap[kmeans.labels_ == i]
        x_i, y_i = weiszfeld(cluster, walls)
        coords.append((x_i, y_i))

    return coords


if __name__ == "__main__":

    width = int(input("Enter width of board: ")) if WIDTH == -1 else WIDTH
    length = int(input("Enter length of board: ")) if LENGTH == -1 else LENGTH
    num_ap = int(input("Enter number of access points: ")) if len(ACCESS_POINTS) == 0 else len(ACCESS_POINTS)
    num_routers = int(input("Enter number of routers: ")) if ROUTERS == -1 else ROUTERS

    if num_routers > num_ap:
        raise ValueError("Number of routers cannot exceed number of access points")

    print("Generating Walls...")
    walls = generate_walls(length, width) if not HAS_WALLS else np.array(WALLS)
    print("Walls Generated")

    print("Generating APs...")
    ap = generate_access_points(num_ap, length, width, walls) if len(ACCESS_POINTS) == 0 else np.array(ACCESS_POINTS)
    print("APs Generated")

    print("Optimizing...")
    start_time = time.time()
    routers = n_routers(num_routers, walls, ap)
    end_time = time.time()
    print("Optimized")

    board = np.zeros((length, width))

    for pt in ap:
        board[pt[0]][pt[1]] = 3

    for pt in walls:
        board[pt[0]][pt[1]] = 4

    for pt in routers:
        board[pt[0]][pt[1]] = 2

    centroid = centroid(ap)
    board[round(centroid[0])][round(centroid[1])] = 4

    plot_grid(board)

    print(f"Program runtime duration: {end_time - start_time}")

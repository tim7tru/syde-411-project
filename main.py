from weiszfeld import *
from plot import *
from wall import *
from sklearn.cluster import KMeans

import time as time
import numpy as np

# Add wall and AP coords here
WALLS = []
ACCESS_POINTS = []


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

    width = int(input("Enter width of board: "))
    length = int(input("Enter length of board: "))
    num_ap = int(input("Enter number of access points: "))
    num_routers = int(input("Enter number of routers: "))

    if num_routers > num_ap:
        raise ValueError("Number of routers cannot exceed number of access points")

    print("Generating Walls...")
    walls = generate_walls(length, width)
    print("Walls Generated")

    print("Generating APs...")
    ap = generate_access_points(num_ap, length, width, walls)
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

    plot_grid(board)

    print(f"Program runtime duration: {end_time - start_time}")

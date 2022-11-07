import random as rand
import numpy as np
import matplotlib as plt
from matplotlib import pyplot


def generate_random_point(max_x, max_y):
    x = rand.randrange(0, max_x, 1)
    y = rand.randrange(0, max_y, 1)
    return x, y


def generate_access_points(n: int, max_length: int, max_width: int):
    if n > max_width * max_length:
        return

    access_points = []

    while len(access_points) < n:
        point = generate_random_point(max_length, max_width)
        if point not in access_points:
            access_points.append(point)

    return np.array(access_points)


def cheb_dist(a: (int, int), b: (int, int)):
    x = abs(a[0] - b[0])
    y = abs(a[1] - b[1])
    return max(x, y)


def weiszfeld(access_points, length, width):
    prev = generate_random_point(length, width)

    for i in range(100):
        dist = []
        for point in access_points:
            dist.append(cheb_dist(prev, point))

        np_dist = np.array([dist, ] * 2).transpose()
        num = (access_points / np_dist).sum(axis=0)
        denom = (np.ones((len(access_points), 2)) / np_dist).sum(axis=0)
        new_point = num / denom
        print(np_dist.mean())
        prev = (new_point[0], new_point[1])

    return round(prev[0]), round(prev[1])

LENGTH = 10
WIDTH = 10

ap = generate_access_points(6, LENGTH, WIDTH)
x, y = weiszfeld(ap, LENGTH, WIDTH)

arr = np.zeros((LENGTH, WIDTH))

for pt in ap:
    arr[pt[0]][pt[1]] = 1
arr[x][y] = 2

cmap = plt.colors.ListedColormap(['black','blue','red'])
bounds = [0,0.5,1.5,2]
norm = plt.colors.BoundaryNorm(bounds, cmap.N)

img = pyplot.imshow(arr, interpolation='nearest', cmap=cmap, norm=norm)

# make a color bar
pyplot.colorbar(img, cmap=cmap, norm=norm, boundaries=bounds, ticks=[0, 1, 2])
pyplot.grid()
pyplot.show()


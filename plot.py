import matplotlib as plt
from matplotlib import pyplot


def plot_grid(arr):
    cmap = plt.colors.ListedColormap(['white', 'blue', 'red', 'green'])
    bounds = [0.5, 1.5, 2.5, 3.5, 4.5]
    norm = plt.colors.BoundaryNorm(bounds, cmap.N)

    img = pyplot.imshow(arr, interpolation='nearest', cmap=cmap, norm=norm)

    # make a color bar
    pyplot.colorbar(img, cmap=cmap, norm=norm, boundaries=bounds, ticks=[0, 1, 2, 3, 4, 5])
    pyplot.show()

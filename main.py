
from enum import Enum
import numpy as np
import numpy.random as npr

import matplotlib.pyplot as plt

from matplotlib import colormaps
print(list(colormaps))

class States(Enum):
    EMPTY = 0
    TREE = 1
    BURNING = 2
    BURNED = 3

enum_to_value = {
    States.EMPTY: 0,
    States.TREE: 1,
    States.BURNING: 2,
    States.BURNED: 3
}

# p = probability
def init_field_on_p(x_size, y_size, prob):
    # Generate the forest
    forest = npr.choice(a=(States.EMPTY, States.TREE),
                        size=(x_size, y_size),
                        p=[1 - prob, prob])

    # Choose a tree
    tree_indexes = np.transpose(np.nonzero(forest))
    burning_tree_index = npr.randint(0, tree_indexes.shape[0])
    y_burning, x_burning = tree_indexes[burning_tree_index]

    # Set a burning tree
    forest[y_burning][x_burning] = States.BURNING

    return forest

def spread_fire(x_size, y_size, x, y, forest) -> bool:
    fire_count = -1
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            x_index = x + i
            y_index = y + j
            if ((i != 0 and j != 0) and
                (x_index < x_size and x_index >= 0) and
                (y_index < y_size and y_index >= 0) and
                (forest[y_index][x_index] == States.TREE)):
                forest[y_index][x_index] = States.BURNING
                fire_count += 1

    forest[y][x] = States.BURNED
    return fire_count

def main(x_size, y_size, p):

    forest = init_field_on_p(x_size, y_size, p)
    fire_count = 1
    step = 0

    while (fire_count > 0):
        for y in range(y_size):
            for x in range(x_size):
                if (forest[y][x] == States.BURNING):
                    fire_count += spread_fire(x_size=x_size,
                                              y_size=y_size,
                                              x=x,
                                              y=y,
                                              forest=forest)

        step += 1
    return forest

def main(x_size, y_size):
    fire_count = 1
    forest = init_field_on_p(100, 100, 0.5)
    step = 0

    while (fire_count > 0):
        for y in range(y_size):
            for x in range(x_size):
                if (forest[y][x] == States.BURNING)
                    fire_count += spread_fire(x=x,
                                              y=y,
                                              forest=forest)
        step += 1

if __name__ == '__main__':
    main()

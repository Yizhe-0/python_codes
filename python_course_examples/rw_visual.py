# @Time: 2020/8/26 12:06
# @Author: Yizhe
# @File: rw_visual.py
# @Software: PyCharm
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
# Make a random walk, and plot the points.
    rw = RandomWalk()
    rw.fill_walk()

    plt.scatter(rw.x_values, rw.y_values, s=10)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
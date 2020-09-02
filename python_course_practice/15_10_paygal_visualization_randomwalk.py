# @Time: 2020/8/29 19:59
# @Author: Yizhe
# @File: 15_10_paygal_visualization_randomwalk.py
# @Software: PyCharm
from random_walk import RandomWalk
import pygal

rw = RandomWalk()
rw.fill_walk()
xy_chart = pygal.XY()
xy_chart.title = 'Random Walk'
rwValues = list(zip(rw.x_values, rw.y_values))
xy_chart.add('rw', rwValues)
xy_chart.render_to_file('rw_visual.svg')

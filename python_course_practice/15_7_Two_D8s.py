# @Time: 2020/8/28 03:11
# @Author: Yizhe
# @File: 15_7_Two_D8s.py
# @Software: PyCharm
import pygal
from die import Die

die_1 = Die()
die_2 = Die()

results = []
for time in range(100000):
    result = die_2.roll() * die_1.roll()
    results.append(result)

frequencies = []
max_number = die_1.num_sides * die_2.num_sides
for value in range(2, max_number+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

hist = pygal.Bar()

hist.title = "Result for two D8 dice rolling 100000 times"
hist.x_labels = [x for x in range(2, 37)]
hist.x_title = "Results"
hist.y_title = "Frequencies of Result"

hist.add("D8 + D8", frequencies)
hist.render_to_file("Roll two D8.svg")
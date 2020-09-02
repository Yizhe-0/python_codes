# @Time: 2020/8/28 10:42
# @Author: Yizhe
# @File: 15_10_Practing_With_Both_Libraries.py
# @Software: PyCharm
from die import Die
import matplotlib.pyplot as plt


die = Die()

plt.figure(dpi=128, figsize=(10, 6))

results = []
for time in range(100000):
    result = die.roll()
    results.append(result)

frequencies = []
max_number = die.num_sides
for value in range(1, max_number+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)


plt.hist(results, bins='auto', rwidth=5, align='left')
plt.show()
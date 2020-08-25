'''
Cubes

Version: 0.1
Author: Yizhe
'''
import pylab
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter

ax = plt.gca()
ax.xaxis.set_major_formatter(FormatStrFormatter('%.0f'))

'''
input_values = [1, 2, 3, 4, 5]
cubes = [1, 8, 27, 64, 125]
'''
input_values = list(range(1, 5000))
cubes = [x**3 for x in input_values]
plt.scatter(input_values, cubes, c=cubes, cmap=plt.cm.Reds, s=5)

plt.show()
print('This is my first on github!')
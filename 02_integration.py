import random
import math
import matplotlib.pyplot as plt
import numpy as np


def integrate(x1, x2, maxmin_steps=100000, iterations=100000, func=lambda x: x ** 2):
    ymin = func(x1)
    ymax = ymin
    for i in xrange(maxmin_steps):
        x = x1 + (x2 - x1) * float(i) / maxmin_steps
        y = func(x)
        if y > ymax:
            ymax = y
        elif y < ymin:
            ymin = y

    area = (x2 - x1) * (ymax - ymin)
    points = 0
    for j in xrange(iterations):
        x = x1 + (x2 - x1) * random.random()
        y = ymin + (ymax - ymin) * random.random()
        if abs(y) <= abs(func(x)):
            if func(x) > 0 and y > 0:
                points += 1
            if func(x) < 0 and y < 0:
                points -= 1

    integral = round(area * float(points) / iterations, 15)
    print 'Integral = %s' % integral


def plot_integral(x1, x2, maxmin_steps=100000, iterations=100000, func=lambda x: x ** 2):
    ymin = func(x1)
    ymax = ymin
    for i in xrange(maxmin_steps):
        x = x1 + (x2 - x1) * float(i) / maxmin_steps
        y = func(x)
        if y > ymax:
            ymax = y
        elif y < ymin:
            ymin = y

    in_x = []
    in_y = []
    for j in xrange(iterations):
        x = x1 + (x2 - x1) * random.random()
        y = ymin + (ymax - ymin) * random.random()
        if abs(y) <= abs(func(x)):
            if (func(x) > 0 and y > 0) or (func(x) < 0 and y < 0):
                in_x.append(x)
                in_y.append(y)

    x = np.linspace(x1, x2, 1000, endpoint=True)
    y = func(x)
    plt.style.use('ggplot')
    plt.plot(x, y, color='#ee2c2c', linewidth=1)
    plt.axhline(0, color='grey')
    plt.plot(in_x, in_y, 'ro', color='#76ee00', markersize=2, label="Points inside circle")
    plt.show()


# integrate(0, 1, 1000000, 1000000, func=lambda x: x ** 2)
# plot_integral(-2, 2, 10000, 10000, func=lambda x: x ** 2)
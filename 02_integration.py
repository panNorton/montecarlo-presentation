import random
import math
import matplotlib.pyplot as plt


# Monte Carlo Methods Presentation
# Example 2 - Integration


def integrate(x1, x2, maxmin_steps=100000, points=100000, func=lambda x: x ** 2):
    """
    Estimates the integral of a function using Monte Carlo methods.

    :param x1: float
        left bound of integration interval
    :param x2: float
        right bound of integration interval
    :param maxmin_steps: int, default 100000
        number of subintervals of [x1, x2] interval
    :param points: int
        Number of randomly generated points from the integration rectangle
    :param func: function
        function to integrate
    """
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
    points_inside = 0
    for j in xrange(points):
        x = x1 + (x2 - x1) * random.random()
        y = ymin + (ymax - ymin) * random.random()
        if abs(y) <= abs(func(x)):
            if func(x) > 0 and y > 0:
                points_inside += 1
            if func(x) < 0 and y < 0:
                points_inside -= 1

    integral = round(area * float(points_inside) / points, 15)
    print 'Integral = %s' % integral


def plot_integral(x1, x2, maxmin_steps=100000, points=100000, func=lambda x: x ** 2):
    """
    Plots the integration process of a function using Monte Carlo methods.
    There is no protection against division by zero etc.

    :param x1: float
        left bound of integration interval
    :param x2: float
        right bound of integration interval
    :param maxmin_steps: int, default 100000
        number of subintervals of [x1, x2] interval
    :param points: int
        Number of randomly generated points from the integration rectangle
    :param func: function
        function to integrate
    """
    ymin = func(x1)
    ymax = ymin
    x_axis = []
    y_axis = []
    for i in xrange(maxmin_steps):
        x = x1 + (x2 - x1) * float(i) / maxmin_steps
        y = func(x)
        x_axis.append(x)
        y_axis.append(y)
        if y > ymax:
            ymax = y
        elif y < ymin:
            ymin = y

    in_x = []
    in_y = []
    out_x = []
    out_y = []
    for j in xrange(points):
        x = x1 + (x2 - x1) * random.random()
        y = ymin + (ymax - ymin) * random.random()
        if abs(y) <= abs(func(x)):
            if (func(x) > 0 and y > 0) or (func(x) < 0 and y < 0):
                in_x.append(x)
                in_y.append(y)
            else:
                out_x.append(x)
                out_y.append(y)
        else:
            out_x.append(x)
            out_y.append(y)

    plt.style.use('ggplot')
    plt.suptitle('Monte Carlo Integration', fontsize=15)
    plt.title('Interval = [%s, %s], Points = %s' % (x1, x2, points))
    plt.plot(x_axis, y_axis, color='#ee2c2c', linewidth=1)
    plt.axhline(0, color='grey')
    plt.plot(in_x, in_y, 'ro', color='#76ee00', markersize=2, label="Points inside integral")
    plt.plot(out_x, out_y, 'ro', color='#ee2c2c', markersize=2, label="Points outside integral")
    plt.ylim(ymin, ymax)
    plt.show()


# integrate(0, 1, 1000000, 1000000, func=lambda x: x ** 2 * math.sin(x))
# plot_integral(-5, 5, 10000, 100000, func=lambda x: math.sin(x))

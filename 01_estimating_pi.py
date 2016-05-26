import random
import math
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def estimate_pi(points=100000):
    """
    Estimates Pi value using Monte Carlo method
    Formula:
    Estimated Pi = 4 * Number of generated points inside a unit circle / Number of generated points

    :param points: positive int, default 100000
        Number of points generated randomly from the set [0,1]x[0,1]
    :return: float
        estimated Pi value
    """
    counter = 0
    for i in xrange(points):
        if math.hypot(random.random(), random.random()) < 1:
            counter += 1
    return 4.0 * counter / points


def plot_estimate_pi(points=100000):
    """
    Plots all points generated by Pi Monte Carlo estimation.

    :param points: positive int, default 100000
        Number of points generated randomly from the set [0,1]x[0,1]
    """
    plt.style.use('ggplot')
    in_x = []
    in_y = []
    out_x = []
    out_y = []
    for i in xrange(points):
        x, y = random.random(), random.random()
        if math.hypot(x, y) < 1:
            in_x.append(x)
            in_y.append(y)
        else:
            out_x.append(x)
            out_y.append(y)

    plt.title('Pi estimation for N = %s points' % points)
    x = np.linspace(0, 1, 1000, endpoint=True)
    y = (1 - x ** 2) ** .5
    plt.plot(x, y, color='grey', linewidth=1) # Plotting unit circle curve
    plt.plot(in_x, in_y, 'ro', color='#76ee00', markersize=2, label="Points inside circle")
    plt.plot(out_x, out_y, 'ro', color='#ee2c2c', markersize=2, label="Points outside circle")
    plt.show()


def n_estimate_pi(tests=100, points=100000):
    """
    Performs n Pi estimations, counting the mean of estimated Pi values
    and a difference from the exact Pi value.
    Increasing points number improves accuracy more than increasing tests number.
    Formula:
    Estimated Pi Mean = Sum of estimated Pi values / Number of tests

    :param tests: positive int, default 100
        Number of tests
    :param points: positive int, default 100000
        Number of points generated randomly from the set [0,1]x[0,1] for every test
    :return: 2-element list
        Estimated Pi Mean, Difference from the exact Pi value
    """
    values = []
    pi_sum = 0.0
    for i in xrange(tests):
        a = estimate_pi(points)
        values.append(a)
        pi_sum += a
    pi_mean = pi_sum / tests
    return pi_mean, abs(math.pi - pi_mean)


def plot_poly3_accuracy_check(iterations=50, tests=10, tests_incr=0, points_first=1000, points_incr=100):
    """
    Checks the accuracy of Pi estimation with different parameters
    and plots the result including 3rd-degree polynomial curve fitting.

    :param iterations: positive int, default 50
        Number of iterations.
    :param tests: positive int, default 10
        Number of tests in a single iteration.
    :param tests_incr: positive int or 0, default 0
        Increment of tests in next iterations.
    :param points_first: positive int, default 1000
        Number of points generated randomly from the set [0,1]x[0,1] in the first test.
    :param points_incr: positive int or 0, default 100
        Increment of points generated randomly from the set [0,1]x[0,1] in next iterations.
    """
    plt.style.use('ggplot')

    accuracies = []
    for i in xrange(iterations):
        accuracies.append(n_estimate_pi(tests=tests + i * tests_incr, points=points_first + i * points_incr)[1])
    # If in need of bigger differences on the plot (to depict the accuracy improvement), one should use:
    # accuracies = map(lambda x: x * 100, accuracies)
    plt.plot(range(len(accuracies)), accuracies, 'ro', color='green', markersize=4, label='Estimated points')

    # Curve fitting
    def func(x, a, b, c, d):
        return a * x ** 3 + b * x ** 2 + c * x + d
    x_axis = np.array(range(len(accuracies)), dtype=float)
    y_axis = np.array(accuracies, dtype=float)
    popt, pcov = curve_fit(func, x_axis, y_axis)
    plt.plot(x_axis, func(x_axis, *popt), color="#ee2c2c", label='Fitted Curve', linewidth=3)
    plt.xlabel('Iterations', fontsize=13)
    plt.ylabel('Difference from Pi value', fontsize=13)
    plt.title('Accuracy check of Monte Carlo Pi estimation \n iterations = %s, tests = %s, tests_incr = %s, '
              'points first = %s, points_incr = %s' % (iterations, tests, tests_incr, points_first, points_incr))
    plt.show()


def plot_linear_accuracy_check(iterations=50, tests=10, tests_incr=0, points_first=1000, points_incr=100):
    """
    Checks the accuracy of Pi estimation with different parameters
    and plots the result including linear (1st degree polynomial) curve fitting.

    :param iterations: positive int, default 50
        Number of iterations.
    :param tests: positive int, default 10
        Number of tests in a single iteration.
    :param tests_incr: positive int or 0, default 0
        Increment of tests in next iterations.
    :param points_first: positive int, default 1000
        Number of points generated randomly from the set [0,1]x[0,1] in the first test.
    :param points_incr: positive int or 0, default 100
        Increment of points generated randomly from the set [0,1]x[0,1] in next iterations.
    """
    plt.style.use('ggplot')

    accuracies = []
    for i in xrange(iterations):
        accuracies.append(n_estimate_pi(tests=tests + i * tests_incr, points=points_first + i * points_incr)[1])
    # If in need of bigger differences on the plot (to depict the accuracy improvement), one should use:
    # accuracies = map(lambda x: x * 100, accuracies)
    plt.plot(range(len(accuracies)), accuracies, 'ro', color='green', markersize=4, label='Estimated points')

    # Curve fitting
    def func(x, c, d):
        return c * x + d
    x_axis = np.array(range(len(accuracies)), dtype=float)
    y_axis = np.array(accuracies, dtype=float)
    popt, pcov = curve_fit(func, x_axis, y_axis)
    plt.plot(x_axis, func(x_axis, *popt), color="#ee2c2c", label='Fitted Curve', linewidth=3)
    plt.xlabel('Iterations', fontsize=13)
    plt.ylabel('Difference from Pi value', fontsize=13)
    plt.title('Accuracy check of Monte Carlo Pi estimation \n iterations = %s, tests = %s, tests_incr = %s, '
              'points first = %s, points_incr = %s' % (iterations, tests, tests_incr, points_first, points_incr))
    plt.show()

# plot_linear_accuracy_check(iterations=100, tests_incr=0, points_first=500, points_incr=100)
# plot_poly3_accuracy_check(iterations=150, tests_incr=0, points_first=500, points_incr=100)
# plot_estimate_pi(points=20000)
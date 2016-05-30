import random
import math
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


# Monte Carlo Methods Presentation
# Example 1 - Pi Estimation


def single_estimate_pi(points=100000):
    """
    Estimates Pi value using Monte Carlo method
    Formula:
    Estimated Pi = 4 * Number of generated points inside a unit circle / Number of generated points

    :param points: positive int, default 100000
        Number of randomly generated points from the set [0,1]x[0,1]
    :return: 2-element list
        Estimated Pi, Difference from the exact Pi value
    """
    counter = 0
    for i in xrange(points):
        if math.hypot(random.random(), random.random()) < 1:
            counter += 1
    est_pi = 4.0 * counter / points
    return est_pi, abs(math.pi - est_pi)


def plot_estimate_pi(points=100000):
    """
    Plots all points generated by Pi Monte Carlo estimation.

    :param points: positive int, default 100000
        Number of randomly generated points from the set [0,1]x[0,1]
    """
    in_x = []
    in_y = []
    out_x = []
    out_y = []
    counter = 0
    for i in xrange(points):
        x, y = random.random(), random.random()
        if math.hypot(x, y) < 1:
            in_x.append(x)
            in_y.append(y)
            counter += 1
        else:
            out_x.append(x)
            out_y.append(y)
    est_pi = round(4.0 * counter / points, 8)
    error = round(abs(math.pi - est_pi), 8)
    plt.style.use('ggplot')
    plt.suptitle('Pi estimation for N = %s points' % points, fontsize=16)
    plt.title('Calculated Pi = %s, Error = %s ' % (est_pi, error), fontsize=12)
    x = np.linspace(0, 1, 1000, endpoint=True)
    y = (1 - x ** 2) ** .5
    plt.plot(x, y, color='grey', linewidth=1)  # Plotting unit circle curve
    plt.plot(in_x, in_y, 'ro', color='#76ee00', markersize=2, label="Points inside circle")
    plt.plot(out_x, out_y, 'ro', color='#ee2c2c', markersize=2, label="Points outside circle")
    plt.show()


def mean_estimate_pi(tests=100, points=100000):
    """
    Performs n Pi estimations, counting the mean of estimated Pi values
    and a difference from the exact Pi value.
    Increasing points number improves accuracy more than increasing tests number.
    Formula:
    Estimated Pi Mean = Sum of estimated Pi values / Number of tests

    :param tests: positive int, default 100
        Number of tests
    :param points: positive int, default 100000
        Number of randomly generated points from the set [0,1]x[0,1] for every test
    :return: 2-element list
        Estimated Pi Mean, Difference from the exact Pi value
    """
    values = []
    pi_sum = 0.0
    for i in xrange(tests):
        a = single_estimate_pi(points)[0]
        values.append(a)
        pi_sum += a
    pi_mean = pi_sum / tests
    return pi_mean, abs(math.pi - pi_mean)


def plot_mean_accuracy_check(iterations=50, points_first=50, points_incr=25, tests=10):
    """
    Checks the accuracy of Pi estimation with single check and mean from n checks
    and plots the result including 3rd-degree polynomial curve fitting.

    :param iterations: positive int, default 50
        Number of iterations.
    :param points_first: positive int, default 50
        Number of randomly generated points from the set [0,1]x[0,1] in the first test.
    :param points_incr: positive int or 0, default 25
        Increment of randomly generated points from the set [0,1]x[0,1] in next iterations.
    :param tests: positive int, default 10
        Number of tests in every mean estimation.
    :return:
    """
    y_axis_single = []
    y_axis_mean = []
    for i in xrange(iterations):
        a = single_estimate_pi(points=points_first + i * points_incr)
        b = mean_estimate_pi(tests=tests, points=points_first + i * points_incr)
        y_axis_single.append(a[1])
        y_axis_mean.append(b[1])

    def func(x, a, b, c, d):
        return a * x ** 3 + b * x ** 2 + c * x + d

    plt.style.use('ggplot')
    plt.title('Accuracy check - single estimation vs. estimation by mean')
    plt.xlabel('Iterations')
    plt.ylabel('Difference from exact Pi value')
    x_axis = np.array(range(iterations), dtype=float)
    y_axis1 = np.array(y_axis_single, dtype=float)
    y_axis2 = np.array(y_axis_mean, dtype=float)
    popt1, pcov1 = curve_fit(func, x_axis, y_axis1)
    plt.plot(x_axis, func(x_axis, *popt1), color="#76ee00", label='Fitted Curve Single', linewidth=3)
    popt2, pcov2 = curve_fit(func, x_axis, y_axis2)
    plt.plot(x_axis, func(x_axis, *popt2), color="#ee2c2c", label='Fitted Curve Mean', linewidth=3)
    plt.plot(x_axis, y_axis_single, 'ro', color='#76ee00', markersize=2)
    plt.plot(x_axis, y_axis_mean, 'ro', color='#ee2c2c', markersize=2)
    plt.legend()
    plt.show()


def accuracy_check(iterations=50, tests=10, tests_incr=0, points_first=1000, points_incr=100, fit_func='linear'):
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
        Number of randomly generated points from the set [0,1]x[0,1] in the first test.
    :param points_incr: positive int or 0, default 100
        Increment of a number of randomly generated points from the set [0,1]x[0,1] in next iterations.
    :param fit_func: string: 'linear', 'poly2', 'poly3', 'poly4', 'poly5'
        Type of a fitted curve.
    """
    accuracies = []
    for i in xrange(iterations):
        accuracies.append(mean_estimate_pi(tests=tests + i * tests_incr, points=points_first + i * points_incr)[1])
    # If in need of bigger differences on the plot (to depict the accuracy improvement), one should use:
    # accuracies = map(lambda x: x * 100, accuracies)
    plt.style.use('ggplot')
    plt.plot(range(len(accuracies)), accuracies, 'ro', color='green', markersize=4, label='Estimated points')

    # Curve fitting
    if fit_func == 'linear':
        def func(x, a, b):
            return a * x + b
    elif fit_func == 'poly2':
        def func(x, a, b, c):
            return a * x ** 2 + b * x + c
    elif fit_func == 'poly3':
        def func(x, a, b, c, d):
            return a * x ** 3 + b * x ** 2 + c * x + d
    elif fit_func == 'poly4':
        def func(x, a, b, c, d, e):
            return a * x ** 4 + b * x ** 3 + c * x ** 2 + d * x + e
    elif fit_func == 'poly5':
        def func(x, a, b, c, d, e, f):
            return a * x ** 5 + b * x ** 4 + c * x ** 3 + d * x ** 2 + e * x + f

    x_axis = np.array(range(len(accuracies)), dtype=float)
    y_axis = np.array(accuracies, dtype=float)
    popt, pcov = curve_fit(func, x_axis, y_axis)
    plt.plot(x_axis, func(x_axis, *popt), color="#ee2c2c", label='Fitted Curve', linewidth=3)
    plt.xlabel('Iterations', fontsize=13)
    plt.ylabel('Difference from Pi value', fontsize=13)
    plt.suptitle('Accuracy check of Monte Carlo Pi estimation', fontsize=15)
    plt.title('iterations = %s, tests = %s, tests_incr = %s, points first = %s, points_incr = %s, fit_func = %s'
              % (iterations, tests, tests_incr, points_first, points_incr, fit_func), fontsize=13)
    plt.show()


accuracy_check(iterations=400, tests_incr=0, points_first=200, points_incr=100, fit_func='poly5')

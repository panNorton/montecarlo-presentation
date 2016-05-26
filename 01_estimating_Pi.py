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
    for i in range(points):
        if math.hypot(random.random(), random.random()) < 1:
            counter += 1
    return 4.0 * counter / points


def n_estimate_pi(tests=100, points=100000):
    """
    Performs n Pi estimations, counting the mean of estimated Pi values and a difference from the exact Pi value.
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
    for i in range(tests):
        a = estimate_pi(points)
        values.append(a)
        pi_sum += a
    pi_mean = pi_sum / tests
    return pi_mean, abs(math.pi - pi_mean)


def plot_accuracy_check(iterations=50, tests=10, points_first=1000, points_increment=100):
    """
    Checks the accuracy of Pi estimation with different parameters and plots the result including curve fitting.
    :param iterations: positive int, default 50
        Number of iterations.
    :param tests: positive int, default 10
        Number of tests in a single iteration.
    :param points_first: positive int, default 1000
        Number of points generated randomly from the set [0,1]x[0,1] for the first test.
    :param points_increment: positive int, default 100
        Increment of points generated randomly from the set [0,1]x[0,1] for next iterations.
    """
    plt.style.use('ggplot')

    accuracies = []
    for i in range(iterations):
        accuracies.append(n_estimate_pi(tests=tests, points=points_first + i * points_increment)[1])
    accuracies = map(lambda x: x * 100, accuracies)
    plt.plot(range(len(accuracies)), accuracies, 'ro', color='green', markersize=5, label="Estimated points")

    # Curve fitting
    def func(x, a, b, c, d):
        return a * x ** 3 + b * x ** 2 + c * x + d
    x_axis = np.array(range(len(accuracies)), dtype=float)
    y_axis = np.array(accuracies, dtype=float)
    popt, pcov = curve_fit(func, x_axis, y_axis)
    plt.plot(x_axis, func(x_axis, *popt), label="Fitted Curve")
    plt.show()

plot_accuracy_check(iterations=70, points_first=1000, points_increment=1000)

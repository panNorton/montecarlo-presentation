import random


def f(x):
    return x ** 3


def integrate(x1, x2, maxmin_steps=100000, iterations=100000):
    ymin = f(x1)
    ymax = ymin
    for i in xrange(maxmin_steps):
        x = x1 + (x2 - x1) * float(i) / maxmin_steps
        y = f(x)
        if y > ymax:
            ymax = y
        elif y < ymin:
            ymin = y

    area = (x2 - x1) * (ymax - ymin)
    points = 0
    for j in xrange(iterations):
        x = x1 + (x2 - x1) * random.random()
        y = ymin + (ymax - ymin) * random.random()
        if abs(y) <= abs(f(x)):
            if f(x) > 0 and y > 0:
                points += 1
            if f(x) < 0 and y < 0:
                points -= 1

    integral = round(area * float(points) / iterations, 15)
    print 'Integral = %s' % integral

# integrate(0, 1, 1000000, 1000000)

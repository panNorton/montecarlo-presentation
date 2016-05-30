import random
import matplotlib.pyplot as plt


# Monte Carlo Method Presentation
# Example 3 - Gambling
# Can also be applied to financial simulations with more sophisticated conditions in gamble()
# Inspired by the tutorial https://pythonprogramming.net/monte-carlo-simulator-python/


def gamble(win_chance=0.5):
    """
    Performs gambling experiment.

    :param win_chance: float (0,1) default 0.5
        Chances of profit in a single bet/period.
    :return: boolean
        True if won, False if lost.
    """
    return True if random.random() <= win_chance else False


def bet(starting_funds=1000, stack=100, win_chance=0.5, periods=100):
    """

    :param starting_funds:
    :param stack:
    :param win_chance:
    :param periods:
    :return:
    """
    funds = starting_funds
    x_axis = [0]
    funds_list = [funds]
    current = 1
    while current <= periods:
        x_axis.append(current)
        if gamble(win_chance):
            funds += stack
            funds_list.append(funds)
        else:
            funds -= stack
            funds_list.append(funds)
        current += 1
    gain = True if funds > starting_funds else False
    broke = True if funds <= 0 else False

    plt.style.use('ggplot')
    plt.plot(x_axis, funds_list)

    return gain, broke


def broke_bet(starting_funds=1000, stack=100, win_chance=0.5, periods=100):
    """

    :param starting_funds:
    :param stack:
    :param win_chance:
    :param periods:
    :return:
    """
    funds = starting_funds
    x_axis = [0]
    funds_list = [funds]
    current = 1
    while current <= periods:
        x_axis.append(current)
        if gamble(win_chance):
            funds += stack
            funds_list.append(funds)
        else:
            funds -= stack
            if funds <= 0:
                funds = 0
                for i in xrange(periods - current):
                    funds_list.append(funds)
                    x_axis.append(current + i)
                current = periods + 1
            funds_list.append(funds)
        current += 1
    gain = True if funds > starting_funds else False
    broke = True if funds <= 0 else False

    plt.style.use('ggplot')
    plt.plot(x_axis, funds_list)

    return gain, broke


def double_bet(starting_funds=10000, stack=100, win_chance=0.5, periods=100):
    """

    :param starting_funds:
    :param stack:
    :param win_chance:
    :param periods:
    :return:
    """
    funds = starting_funds
    x_axis = [0]
    funds_list = [funds]
    current = 1
    lost_count = 0
    while current <= periods:
        x_axis.append(current)
        if lost_count == 0:
            if gamble(win_chance):
                funds += stack
                funds_list.append(funds)
            else:
                funds -= stack
                funds_list.append(funds)
                lost_count += 1
        else:
            if gamble(win_chance):
                funds += 2 ** lost_count * stack
                funds_list.append(funds)
                lost_count = 0
            else:
                funds -= 2 ** lost_count * stack
                funds_list.append(funds)
                lost_count += 1
        current += 1
    gain = True if funds > starting_funds else False
    broke = True if funds <= 0 else False

    plt.style.use('ggplot')
    plt.plot(x_axis, funds_list)

    return gain, broke


def double_broke_bet(starting_funds=10000, stack=100, win_chance=0.5, periods=100):
    """

    :param starting_funds:
    :param stack:
    :param win_chance:
    :param periods:
    :return:
    """
    funds = starting_funds
    x_axis = [0]
    funds_list = [funds]
    current = 1
    lost_count = 0
    while current <= periods:
        x_axis.append(current)
        if lost_count == 0:
            if gamble(win_chance):
                funds += stack
                funds_list.append(funds)
            else:
                funds -= stack
                if funds <= 0:
                    funds = 0
                    for i in xrange(periods - current):
                        funds_list.append(funds)
                        x_axis.append(current + i)
                    current = periods + 1
                funds_list.append(funds)
                lost_count += 1
        else:
            if gamble(win_chance):
                funds += 2 ** lost_count * stack
                funds_list.append(funds)
                lost_count = 0
            else:
                funds -= 2 ** lost_count * stack
                if funds <= 0:
                    funds = 0
                    for i in xrange(periods - current):
                        funds_list.append(funds)
                        x_axis.append(current + i)
                    current = periods + 1
                funds_list.append(funds)
                lost_count += 1
        current += 1
    gain = True if funds > starting_funds else False
    broke = True if funds <= 0 else False

    plt.style.use('ggplot')
    plt.plot(x_axis, funds_list)

    return gain, broke


def simul_bets(bettors=1000, starting_funds=1000, stack=100, win_chance=0.5, periods=100, double=False):
    """

    :param bettors:
    :param starting_funds:
    :param stack:
    :param win_chance:
    :param periods:
    :param double:
    :return:
    """
    x = 0
    gains = 0
    broke = 0
    if double:
        while x < bettors:
            a = double_bet(starting_funds, stack, win_chance, periods)
            if a[0]:
                gains += 1
            if a[1]:
                broke += 1
            x += 1
    else:
        while x < bettors:
            a = bet(starting_funds, stack, win_chance, periods)
            if a[0]:
                gains += 1
            if a[1]:
                broke += 1
            x += 1
    gains_percent = round(100.0 * gains / bettors, 4)
    broke_percent = round(100.0 * broke / bettors, 4)
    plt.suptitle('Betting simulation of %s bettors: Starting funds = %s, Stack = %s, Win chance = %s %%, double = %s'
                 % (bettors, starting_funds, stack, win_chance * 100, double), fontsize=15)
    plt.title('Profit = %s %%, Loss = %s %%, Broke = %s %%' %
              (gains_percent, 100.0 - gains_percent, broke_percent), fontsize=15)
    plt.xlabel('Periods', fontsize=13)
    plt.ylabel('Funds', fontsize=13)
    plt.show()


def simul_broke_bets(bettors=1000, starting_funds=1000, stack=100, win_chance=0.5, periods=100, double=False):
    """

    :param bettors:
    :param starting_funds:
    :param stack:
    :param win_chance:
    :param periods:
    :param double:
    :return:
    """
    x = 0
    gains = 0
    broke = 0
    if double:
        while x < bettors:
            a = double_broke_bet(starting_funds, stack, win_chance, periods)
            if a[0]:
                gains += 1
            if a[1]:
                broke += 1
            x += 1
    else:
        while x < bettors:
            a = broke_bet(starting_funds, stack, win_chance, periods)
            if a[0]:
                gains += 1
            if a[1]:
                broke += 1
            x += 1
    gains_percent = round(100.0 * gains / bettors, 4)
    broke_percent = round(100.0 * broke / bettors, 4)
    plt.suptitle('Betting simulation of %s bettors: Starting funds = %s, Stack = %s, Win chance = %s %%, Double = %s'
                 % (bettors, starting_funds, stack, win_chance * 100, double), fontsize=15)
    plt.title('Profit = %s %%, Loss = %s %%, Broke = %s %%' %
              (gains_percent, 100.0 - gains_percent, broke_percent), fontsize=15)
    plt.xlabel('Periods', fontsize=13)
    plt.ylabel('Funds', fontsize=13)
    plt.show()


# simul_bets(bettors=500, starting_funds=1000, stack=100, win_chance=0.48, periods=10000, double=False)
# simul_broke_bets(bettors=500, starting_funds=10000, stack=100, win_chance=0.49, periods=10000, double=True)
# double_broke_bet(stack=200, periods=1000)

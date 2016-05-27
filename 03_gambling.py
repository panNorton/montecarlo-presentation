import random
import matplotlib.pyplot as plt

# Inspired by this tutorial https://pythonprogramming.net/monte-carlo-simulator-python/


def gamble(win_chance=0.5):
    if random.random() <= win_chance:
        return True
    else:
        return False


def broke_bet(starting_funds=1000, stack=100, win_chance=0.5, periods=100):
    funds = starting_funds
    x_axis = []
    funds_list = []
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


def bet(starting_funds=1000, stack=100, win_chance=0.5, periods=100):
    funds = starting_funds
    x_axis = []
    funds_list = []
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


def simul_bets(bettors=1000, starting_funds=1000, stack=100, win_chance=0.5, periods=100):
    x = 0
    gains = 0
    broke = 0
    while x < bettors:
        a = bet(starting_funds, stack, win_chance, periods)
        if a[0]:
            gains += 1
        if a[1]:
            broke += 1
        x += 1
    gains_percent = round(100.0 * gains / bettors, 4)
    broke_percent = round(100.0 * broke / bettors, 4)
    plt.suptitle('Betting simulation of %s bettors: Starting funds = %s, Stack = %s, Win chance = %s %%'
                 % (bettors, starting_funds, stack, win_chance * 100), fontsize=15)
    plt.title('Profit = %s %%, Loss = %s %%, Broke = %s %%' %
              (gains_percent, 100.0 - gains_percent, broke_percent), fontsize=15)
    plt.xlabel('Periods', fontsize=13)
    plt.ylabel('Funds', fontsize=13)
    plt.show()


def simul_broke_bets(bettors=1000, starting_funds=1000, stack=100, win_chance=0.5, periods=100):
    x = 0
    gains = 0
    broke = 0
    while x < bettors:
        a = broke_bet(starting_funds, stack, win_chance, periods)
        if a[0]:
            gains += 1
        if a[1]:
            broke += 1
        x += 1
    gains_percent = round(100.0 * gains / bettors, 4)
    broke_percent = round(100.0 * broke / bettors, 4)
    plt.suptitle('Betting simulation of %s bettors: Starting funds = %s, Stack = %s, Win chance = %s %%'
                 % (bettors, starting_funds, stack, win_chance * 100), fontsize=15)
    plt.title('Profit = %s %%, Loss = %s %%, Broke = %s %%' %
              (gains_percent, 100.0 - gains_percent, broke_percent), fontsize=15)
    plt.xlabel('Periods', fontsize=13)
    plt.ylabel('Funds', fontsize=13)
    plt.show()


# simul_bets(bettors=900, starting_funds=10000, stack=100, win_chance=0.5, periods=900)
simul_broke_bets(bettors=900, starting_funds=10000, stack=100, win_chance=0.495, periods=900)

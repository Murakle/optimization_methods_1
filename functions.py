import math

def f1(x):
    return -5 * x ** 5 + 4 * x ** 4 - 12 * x ** 3 + 11 * x ** 2 - 2 * x + 1


def f2(x):
    return math.log(x - 2, 2) ** 2 + math.log(10 - x, 2) ** 2 - x ** 0.2


def f3(x):
    return -3 * x * math.sin(0.75 * x) + math.exp(- 2 * x)


def f4(x):
    return math.exp(3 * x) + 5 * math.exp(-2 * x)


def f5(x):
    return 0.2 * x * math.log(x, 2) + (x - 2.3) ** 2


def testF(x):
    return x ** 4 + math.exp(-x)


def testInterval():
    return [0, 1]

def interval1():
    return [-0.5, 0.5]


def interval2():
    return [6, 9.9]


def interval3():
    return [0, 2 * math.pi]


def interval4():
    return [0, 1]


def interval5():
    return [0.5, 2.5]


functions = [f1, f2, f3, f4, f5]
intervals = [interval1, interval2, interval3, interval4, interval5, testInterval]


def getFunctionsAmount():
    return len(functions)


# index - index of function [0;4]
def getF(x, index):
    return functions[index](x)


# index - index of function [0;4]
def getInterval(index):
    return intervals[index]()

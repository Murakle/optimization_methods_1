from functions import getInterval, getF
import math


def print_with_tabs(*arg):
    for a in arg:
        print(str(a).replace(".", ","), end="\t")
    print("")


"""
   :arg     index - index of function [0;4], eps - accuracy, beta < eps/2
   :return  { center of interval of length eps, amount of F calls}
"""


def dichotomy(index, eps, printAll=False):
    beta = eps / 3
    interval = getInterval(index)
    a = interval[0]
    b = interval[1]
    function_calls = 0
    if printAll:
        print_with_tabs("Dichotomy", "eps=", eps, "Func index=", index)
        print_with_tabs("a", "b", "x1", "x2", "f1", "f2", "function_calls", "b - a")
    while b - a > eps:
        m = (a + b) / 2
        x1 = m - beta
        x2 = m + beta
        f1 = getF(x1, index)
        f2 = getF(x2, index)
        function_calls += 2
        if printAll:
            print_with_tabs(a, b, x1, x2, f1, f2, function_calls, b - a)
        if f1 >= f2:
            a = x1
        if f1 <= f2:
            b = x2
    if printAll:
        print_with_tabs(a, b, x1, x2, f1, f2, function_calls, b - a)
    return [(a + b) / 2, function_calls]
    # return function_calls


def golden_ratio(index, eps, printAll=False):
    interval = getInterval(index)
    a = interval[0]
    b = interval[1]
    c = (math.sqrt(5) - 1) / 2
    x1 = a + c * (b - a)
    x2 = b - c * (b - a)
    f1 = getF(x1, index)
    f2 = getF(x2, index)
    function_calls = 2
    if printAll:
        print_with_tabs("Golden ratio", "eps=", eps, "Func index=", index)
        print_with_tabs("a", "b", "x1", "x2", "f1", "f2", "function_calls", "b - a")
    while b - a > eps:
        if x1 > x2:  # swap
            x1, x2 = x2, x1
            f1, f2 = f2, f1
        if printAll:
            print_with_tabs(a, b, x1, x2, f1, f2, function_calls, b - a)
        if f1 > f2:
            a = x1
            x1 = x2
            f1 = f2
            x2 = b - (x1 - a)
            if b - a <= eps:
                break
            f2 = getF(x2, index)
            function_calls += 1
        else:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + (b - x2)
            if b - a <= eps:
                break
            f1 = getF(x1, index)
            function_calls += 1
    if printAll:
        print_with_tabs(a, b, x1, x2, f1, f2, function_calls, b - a)
    return [(a + b) / 2, function_calls]
    # return function_calls


def getFibonachiNumber(n):
    return 1 / math.sqrt(5) * ((((1 + math.sqrt(5)) / 2)) ** n - (((1 - math.sqrt(5)) / 2)) ** n)


def findN(a, b, eps):
    i = 0
    while getFibonachiNumber(i + 2) <= (b - a) / eps:
        i += 1
    return i + 1


def fibonachi(index, eps, printAll=False):
    interval = getInterval(index)
    a = interval[0]
    b = interval[1]
    n = findN(a, b, eps)
    x1 = a + getFibonachiNumber(n) / getFibonachiNumber(n + 2) * (b - a)
    x2 = a + getFibonachiNumber(n + 1) / getFibonachiNumber(n + 2) * (b - a)
    f1 = getF(x1, index)
    f2 = getF(x2, index)
    function_calls = 2
    k = 1
    if printAll:
        print_with_tabs("Fibanachi", "eps=", eps, "Func index=", index)
        print_with_tabs("a", "b", "x1", "x2", "f1", "f2", "function_calls", "b - a")
    while b - a > eps:
        if x1 > x2:  # swap
            x1, x2 = x2, x1
            f1, f2 = f2, f1
        if printAll:
            print_with_tabs(a, b, x1, x2, f1, f2, function_calls, b - a)
        if f1 > f2:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + getFibonachiNumber(n - k + 2)/getFibonachiNumber(n - k + 3)* (b - a)
            if b - a <= eps:
                break
            f2 = getF(x2, index)
            function_calls += 1
        else:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + getFibonachiNumber(n - k + 1)/getFibonachiNumber(n - k + 3)* (b - a)
            if b - a <= eps:
                break
            f1 = getF(x1, index)
            function_calls += 1
        k += 1
    if printAll:
        print_with_tabs(a, b, x1, x2, f1, f2, function_calls, b - a)
    return [(a + b) / 2, function_calls]
    # return function_calls


def parabola(index, eps, printAll=False):
    interval = getInterval(index)
    a = interval[0]  # x1
    b = interval[1]  # x3
    x1 = (a + b) / 2  # x2
    fa = getF(a, index)  # f1
    fb = getF(b, index)  # f3
    f1 = getF(x1, index)  # f2
    x2 = x1 - ((x1 - a) ** 2 * (f1 - fb) - (x1 - b) ** 2 * (f1 - fa)) \
         / (2 * ((x1 - a) * (f1 - fb) - (x1 - b) * (f1 - fa)))
    f2 = getF(x2, index)
    if x1 > x2:  # swap
        x1, x2 = x2, x1
        f1, f2 = f2, f1
    function_calls = 4
    max_function_calls = 500
    if printAll:
        print_with_tabs("Parabola", "eps=", eps, "Func index=", index)
        print_with_tabs("a", "b", "x1", "x2", "f1", "f2", "function_calls", "b - a")
    while function_calls < max_function_calls:
        if x1 > x2:  # swap
            x1, x2 = x2, x1
            f1, f2 = f2, f1
        if printAll:
            print_with_tabs(a, b, x1, x2, f1, f2, function_calls, b - a)
        if f1 >= f2:
            a = x1
            fa = f1
            x1 = x2
            f1 = f2
            if (x1 - a) * (f1 - fb) - (x1 - b) * (f1 - fa) == 0:
                break
            x2 = x1 - ((x1 - a) ** 2 * (f1 - fb) - (x1 - b) ** 2 * (f1 - fa)) \
                 / (2 * ((x1 - a) * (f1 - fb) - (x1 - b) * (f1 - fa)))
            if b - a <= eps:
                break
            f2 = getF(x2, index)
            function_calls += 1
        else:
            b = x2
            fb = f2
            x2 = x1
            f2 = f1
            prev_min_x = x1
            if (x2 - a) * (f2 - fb) - (x2 - b) * (f2 - fa) == 0:
                break
            x1 = x2 - ((x2 - a) ** 2 * (f2 - fb) - (x2 - b) ** 2 * (f2 - fa)) \
                 / (2 * ((x2 - a) * (f2 - fb) - (x2 - b) * (f2 - fa)))
            if abs(b - a) <= eps:
                break
            f1 = getF(x1, index)
            function_calls += 1
    if printAll:
        print_with_tabs(a, b, x1, x2, f1, f2, function_calls, b - a)
    return [(a + b) / 2, function_calls]
    # return function_calls


def brent(index, eps, printAll=False):
    interval = getInterval(index)
    a = interval[0]
    c = interval[1]
    K = (3 - math.sqrt(5)) / 2
    x = w = v = (a + c) / 2
    fx = fw = fv = getF(x, index)
    d = e = c - a
    function_calls = 1
    if printAll:
        print_with_tabs("Brent", "eps=", eps, "Func index=", index)
        print_with_tabs("a", "c", "x", "w", "v", "fx", "fw", "fv", "d", "e", "u", "fu", "function_calls",
                        "current_method")
    while c - a > eps:
        m = 0.5 * (a + c)
        # if abs(x - m) <= 2 * eps - 0.5 * (c - a):
        #     break
        current_method = "parabola"
        g = e
        e = d
        u = c + eps
        if ((w - x) * (fw - fv) - (w - v) * (fw - fx)) != 0:
            u = w - ((w - x) ** 2 * (fw - fv) - (w - v) ** 2 * (fw - fx)) \
                / (2 * ((w - x) * (fw - fv) - (w - v) * (fw - fx)))
        if u + eps <= c and u - eps >= a and abs(u - x) < g / 2:
            d = c - x
        else:
            current_method = "golden"
            if x < (c + a) / 2:
                u = x + K * (c - x)
                d = c - x
            else:
                u = x - K * (x - a)
                d = x - a
        # if abs(u - x) < eps:
        #     u = x + eps if (u - x > 0) else x - eps
        fu = getF(u, index)
        function_calls += 1
        if printAll:
            print_with_tabs(a, c, x, w, v, fx, fw, fv, d, e, u, fu, function_calls, current_method)
        if fu <= fx:
            if u >= x:
                a = x
            else:
                c = x
            v = w
            w = x
            x = u
            fv = fw
            fw = fx
            fx = fu
        else:
            if u >= x:
                c = u
            else:
                a = u
            if fu <= fw or w == x:
                v = w
                w = u
                fv = fw
                fw = fu
            elif fu <= fv or v == x or v == w:
                v = u
                fv = fu
    if printAll:
        print_with_tabs(a, c, x, w, v, fx, fw, fv, d, e, u, fu, function_calls, current_method)
    return [x, function_calls]
    # return function_calls

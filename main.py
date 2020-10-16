from functions import getFunctionsAmount
import methods
import matplotlib.pyplot as plt
from math import sqrt
import sys

methods_names = ["Дихотомии", "Фибоначи", "Золотого сечения", "Параболы", "Брента"]
if __name__ == '__main__':
    functionsAmount = getFunctionsAmount()
    epsAmount = 7 #7
    answers = [] * epsAmount
    # from 1e-1 to 1e-8
    x = [0.0] * epsAmount
    printAll = False
    original_stdout = sys.stdout
    with open('method_output.txt', 'w+') as f:
        sys.stdout = f
        for j in range(1, epsAmount + 1):
            eps = 0.1 ** j
            x[j - 1] = j
            matrix = [] * functionsAmount
            # print(eps)
            for i in range(0, functionsAmount):
                row = [methods.dichotomy(i, eps, False), methods.fibonachi(i, eps, True),
                       methods.golden_ratio(i, eps, False), methods.parabola(i, eps, False),
                       methods.brent(i, eps, False)]
                # print(row)
                matrix.append(row)
            answers.append(matrix)
        methods_amount = 5
        sys.stdout = original_stdout

    # '''graphics
    for k in range(0, 5):
        for i in range(0, functionsAmount):
            y = [0.0] * epsAmount
            for j in range(1, epsAmount + 1):
                y[j - 1] = answers[j - 1][i][k][1]
            l = 'f' + str(i + 1)
            plt.plot(x, y, marker='o', label=l)
        plt.xlabel('Точность = 0.1^x')
        plt.ylabel('Количество вызовов функции')
        plt.title('Метод ' + methods_names[k])
        plt.legend()
        plt.show()
    # 1
    for k in range(0, 5):
        y = [0.0] * epsAmount
        for j in range(1, epsAmount + 1):
            sum = 0
            for i in range(0, functionsAmount):
                sum += answers[j - 1][i][k][1] #** 2
            # y[j - 1] = sqrt(sum/ functionsAmount)
            y[j - 1] = sum / functionsAmount
        plt.plot(x, y, marker='o', label='Метод ' + methods_names[k])
    plt.xlabel('Точность = 0.1^x')
    # plt.yscale('log', basey=2)
    plt.ylabel('Средне количество вызовов функции')
    plt.title('График зависимости среднего количества \nвызовов функции от погрешности')
    plt.legend()
    plt.show()
    # '''

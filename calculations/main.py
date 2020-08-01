import matplotlib.pyplot as plt
import numpy as np
from inspect import getsourcelines


# def plottaren(funktion, start, slut, noggrannhet):
#     x1 = np.linspace(start, slut, noggrannhet)
#     y = np.zeros(noggrannhet)
#     for i, x in enumerate(x1):
#         y[i] = eval(funktion)
#     plt.figure()
#     plt.plot(y)
#     plt.show()
#
#
# plottaren("x**2", 0, 10, 100)


def plottaren(funktion, start, slut, noggrannhet):
    x = np.linspace(start, slut, noggrannhet)
    y = funktion(x)
    fig = plt.figure(figsize=(10, 5))
    plt.title('En funktion')
    plt.xlabel('Tid')
    plt.ylabel('Sträcka')
    plt.plot(x, y, 'g', label=getsourcelines(funktion))
    plt.legend()
    plt.grid(True)
    plt.show()


def ekvation(x):
    return np.sin(x ** 3 / 5) * 20


plottaren(lambda x: ekvation(x), 0, 10, 1000)

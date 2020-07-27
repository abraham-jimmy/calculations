import matplotlib.pyplot as plt
import numpy as np




def plottaren(funktion, start, slut, noggrannhet):
    x1 = np.linspace(start, slut, noggrannhet)
    y = np.zeros(noggrannhet)
    for i, x in enumerate(x1):
        y[i] = eval(funktion)
    plt.figure()
    plt.plot(y)
    plt.show()


plottaren("x**2", 0, 10, 100)










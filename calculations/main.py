import matplotlib.pyplot as plt
import numpy as np
from inspect import getsourcelines


def plottaren(funktion, start=0, end=5, points=1000, plot=True, block=True, legend:str=None, title:str=None,
              xlabel:str=None, ylabel:str=None):
    """
    Calculate a function and draw a diagram. Returns function values in y and x.

    :rtype: tuple[np.ndarray, np.ndarray]
    """
    assert start < end

    x = np.linspace(start, end, points)

    if funktion.__class__.__name__ == "str":
        y = eval(funktion)
        label = format(funktion)

    elif funktion.__class__.__name__ == "function":
        y = funktion(x)
        label = getsourcelines(funktion)

    else:
        raise AttributeError(f"Got {funktion} but this is not a parameter nor a string")

    if legend is not None:
        label = legend
    if plot:
        plt.figure(figsize=(10, 5))
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.plot(x, y, 'g', label=label)
        plt.legend()
        plt.grid(True)
        plt.show(block=block)

    return x, y


# plottaren("x**2", block=False, title="En Titel")
# plottaren(lambda x: x ** 2, legend="x^2")

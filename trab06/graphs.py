import matplotlib.pyplot as plt
import numpy as np


def dispersion1(x:np.ndarray, y:np.ndarray, a:float, b:float,title:str, color = "g-"):
    plt.scatter(x,y)
    plt.plot([x.min(),x.max()], [b * x.min() + a, b * x.max() + a], color)

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(title)

    plt.show()

def dispersion2(x:np.ndarray, y:np.ndarray, a1:float, b1:float,label1, a2:float, b2:float, label2:str, color1:str = "g-", color2:str = "r-", title:str = "Comparisson of results"):
    plt.scatter(x,y)
    plt.plot([x.min(), x.max()], [b1 * x.min() + a1, b1 * x.max() + a1], color1, label = label1)
    plt.plot([x.min(), x.max()], [b2 * x.min() + a2, b2 * x.max() + a2], color2, label = label2)

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(title)

    plt.legend(loc='best')
    plt.show()
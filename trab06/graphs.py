import matplotlib.pyplot as plt
import numpy as np




def dispersion(x:np.ndarray, y:np.ndarray, a1:float, b1:float, a2:float, b2:float):
    plt.scatter(x,y)
    plt.plot([x.min(),x.max()], [b1 * x.min() + a1, b1 * x.max() + a1],"g-")
    plt.plot([x.min(),x.max()], [b2 * x.min() + a2, b2 * x.max() + a2],"r-")
    plt.show()
import matplotlib.pyplot as plt
import numpy as np




def dispersion(x:np.ndarray, y:np.ndarray, a:float, b:float):
    print("entrou")
    plt.scatter(x,y)
    plt.plot([x.min(),x.max()], [a * x.min() + b, a * x.max() + b])
    plt.show()
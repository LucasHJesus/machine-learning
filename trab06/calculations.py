import pandas as pd
import numpy as np
import graphs as gra


#(n(Σxy)+ΣxΣy)/(nΣ(x^2)-(Σx)^2)

def coeficients(x:np.ndarray, y:np.ndarray) -> float:
    y_mean = np.mean(y)
    x_mean = np.mean(x)
    n = x.size
    sum_prod = np.sum(x*y)
    prod_sum = np.sum(x) * np.sum(y)
    sum_srqed = np.sum(x**2)
    sqred_sum = np.sum(x)**2

    b = ((n * sum_prod - prod_sum)/(n * sum_srqed - sqred_sum))

    a = y_mean - b * x_mean
    return (a, b)







if __name__ =="__main__":
    df = pd.read_csv("basedeobservacoes.txt", sep=",")
    x = np.array( df["x"].tolist())
    y = np.array( df["y"].tolist())
    a,b = coeficients(x,y)
    print(f"a: {a}\tb: {b}")
    gra.dispersion(x,y,a,b)

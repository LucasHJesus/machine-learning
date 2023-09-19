import pandas as pd
import numpy as np
import graphs 
import math


#(n(Σxy)+ΣxΣy)/(nΣ(x^2)-(Σx)^2)

def linear_reg(x:np.ndarray, y:np.ndarray) -> float:
    y_mean = np.mean(y)
    x_mean = np.mean(x)
    n = x.size
    sum_prod = np.sum(x * y)
    prod_sum = np.sum(x) * np.sum(y)
    sum_srqed = np.sum(x**2)
    sqred_sum = np.sum(x)**2

    b = ((n * sum_prod - prod_sum)/(n * sum_srqed - sqred_sum))

    a = y_mean - b * x_mean
    return (a, b)


def pearson(x:np.ndarray,y:np.ndarray) -> float:
    n = x.size
    sum_prod = np.sum(x * y)
    prod_sum = np.sum(x) * np.sum(y)

    sum_srqed_x = np.sum(x**2)
    sqred_sum_x = np.sum(x)**2
    sum_srqed_y = np.sum(y**2)
    sqred_sum_y = np.sum(y)**2

    numerator = n * sum_prod - prod_sum
    denominator = math.sqrt(n * sum_srqed_x - sqred_sum_x) *  math.sqrt(n * sum_srqed_y - sqred_sum_y)

    r = numerator / denominator

    return r


def determination_coef(x:np.ndarray, y:np.ndarray) -> float:
    return pearson(x,y)**2



if __name__ =="__main__":
    df = pd.read_csv("basedeobservacoes.txt", sep=",")
    x = np.array( df["x"].tolist())
    y = np.array( df["y"].tolist())
    a,b = linear_reg(x,y)
    print(f"a: {a}\tb: {b}")
    print(f"pearson: {pearson(x,y)}\tcoeficiente de determinante: {determination_coef(x,y)}")
    graphs.dispersion(x,y,a,b)

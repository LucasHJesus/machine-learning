import pandas as pd
import numpy as np
import random
import math
import graphs
import calculations

class adaline():
    def __init__(self) -> None:
        pass

    def __activate(self, x:float):
        return x * self.weights[0] + self.weights[1]

    def __error(self, target:int, y_in:float) -> float:
        return (target - y_in)*(target - y_in)
    
    def __update_weight(self, old:float, target:int, x_in:float, y_in:int) -> float:
        return old + self.learnin_rate * (target - y_in) * x_in

    def training(self, x:np.ndarray, y:np.ndarray, learnin_rate:float = 0.001, max_error:float = 2, max_epoch:int = 100) -> tuple:

        self.learnin_rate:float = learnin_rate
        self.max_error:float = max_error
        self.max_epoch:int = max_epoch
        
        epoch = 0
        error:float = self.max_error + 1.00
        self.weights = [(random.random() - 0.5) for _ in range(2) ]

        print("training started")
        while(error > self.max_error and epoch < self.max_epoch):
            error=0
            epoch += 1
            for i in range(x.size):
                y_in = self.__activate(x[i])
                error += self.__error(target = y[i], y_in = y_in)
                self.weights[0] = self.__update_weight(old = self.weights[0], target = y[i], x_in=x[i], y_in = y_in)
                self.weights[1] = self.__update_weight(old = self.weights[1], target = y[i], x_in=1, y_in = y_in)
            print(f"epoca: {epoch}\tpesos: {self.weights}\t error: {error}")

        return (self.weights[0],self.weights[1])
    



if __name__ == "__main__":

    df = pd.read_csv("basedeobservacoes.txt", sep=",")
    
    x = np.array( df["x"].tolist())
    y = np.array( df["y"].tolist())
    
    neuronio = adaline()
    a1, b1 = neuronio.training(x = x, y = y, max_epoch = 1000, learnin_rate = 0.0001)
    a2, b2 = calculations.linear_reg(x = x, y = y)

    print(f"a1: {a1}\tb1: {b1}")
    print(f"a2: {a2}\tb2: {b2}")
    graphs.dispersion1(x = x, y = x, a = a1, b = b1, color = "g-")
    graphs.dispersion1(x = x, y = x, a = a2, b = b2, color = "r-")
    graphs.dispersion2(x = x, y = x, a1 = a1, b1 = b1, a2 = a2, b2 = b2, color1 = "r-", color2 = "g-")





""" print(df)

    for i in range(x.size):
        print(f"i:{i}\t{x[i]}\t{y[i]}") """

""" size = 0
    training_set = []
    x_training = []
    y_training = []
    x_test = []
    y_test = [] """


"""     while(size < math.ceil(0.8 * x.size)):
        number = random.randint(0,x.size)
        if number not in training_set:
            training_set.append(number)
            size+=1

    for i in range(x.size):
        if i in training_set:
            x_training.append(x[i])
            y_training.append(y[i])
        else:
            x_test.append(x[i])
            y_test.append(y[i])

    x_training = np.array(x_training)
    y_training = np.array(y_training)
    x_test = np.array(x_test)
    y_test = np.array(y_test) """
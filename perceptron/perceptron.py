import random
import numpy as np


class perceptron:

    def __step__(input:float) -> int:
        return 1 if input>=0 else -1
    
    def __error__() -> float:
        pass

    def __init__(self, inputSize:int, alph:float) -> None:
        self.weights = np.array([random.random()-0.5 for _ in range(inputSize)])
        self.alpha = alph
        self.maxEpoch = 100
        pass

    def train(self, dataset:list, target:int) -> bool:
        dataset = self.__linearize__(dataset)
        data = np.array(dataset)
        for i in range(self.maxEpoch):
            for j in range(len(data.size)):
                np.dot(data,self.weights)
                
    def __linearize__(matrix:list) -> list:
        output:list
        output = []
        for line in matrix:
            for item in line:
                output.append(item)
        return output
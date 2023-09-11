import random
import numpy as np


class neuron:

    def __init__(self, inputSize:int, theta:int) -> None:
        self.theta=theta 
        self.inWeights:list = np.array([random.random()-0.5 for _ in range(inputSize)])
        self.inputs:list
        pass
    
    def __step__(input:float) -> int:
        return 1 if input>=0 else -1
    
    def isActive(self):
        sum:float = 0
        for i in range(len(self.inWeights)):
            sum += self.inWeights[i]*self.inputs[i]
        return self.__step__(sum)


class perceptron:
    
    def __error__() -> float:
        pass

    def __init__(self, inputSize:int, alph:float) -> None:
        neuronT:neuron
        neuronX:neuron
        self.alpha = alph
        self.maxEpoch = 100
        pass

    def __linearize__(matrix:list) -> list:
        output:list
        output = []
        for line in matrix:
            for item in line:
                output.append(item)
        return output

    def training(self, dataset:list, target:int) -> bool:
        for itemData,itemTarget in zip(dataset,target):
            for i in range(self.maxEpoch):
                for i,j in zip(itemData,itemTarget):



        pass
                

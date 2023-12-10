import math, random
import matplotlib.pyplot as plt
import numpy as np

def rastringFunction(x:list):
    res = 10 * len(x)
    for i in x:
        res+=i**2 - 10 * math.cos(2 * math.pi * i)

    return res


lowerBound=-5
upperBound=5
function=rastringFunction
populationSize=8 
F = 0.5
Pcr = 0.7
maxEpoch = 1000
historico = []

epoch = 0

try:
    alvo = []
    for _ in range(populationSize): 
        alvo.append( random.sample(range(lowerBound,upperBound), 2))


    while(1):
        for i in range(populationSize):
            for j in range(len(alvo[i])):
                r_vec = random.sample(range(0,len(alvo)), 3)

                while i in r_vec:
                    r_vec = random.sample(range(0,populationSize), 3)

                u_i_j = alvo[r_vec[0]][j] + F * (alvo[r_vec[1]][j] - alvo[r_vec[2]][j])

                s = random.random()
                X_i_j = []
                temp = alvo.copy()
                if s > Pcr:
                    
                    X_i_j = temp[i].copy()
                    
                    X_i_j[j] = u_i_j
                    #X_i_j = u_i_j
                else:
                    X_i_j = temp[i]

                f_X_i_j = function(X_i_j)
                f_alvo = function(alvo[i])

                if f_X_i_j < f_alvo:
                    #print(f"function(X_i_j):{function(X_i_j)}\t  function(alvo[i]){function(alvo[i])}")
                    alvo[i] = X_i_j
        
        output1 = []

        for i in range(len(alvo)):
            output1.append(function(alvo[i]))
        
        minIndex1 = output1.index(min(output1))
        historico.append(output1[minIndex1])

        if epoch % 100 == 0:
            
            print(f"epoch: {epoch}\t minimo: {output1[minIndex1]} dominio: {alvo[minIndex1]}")
            
        if epoch == maxEpoch:
            break
        epoch+=1
    
    output = []

    for i in range(len(alvo)):
        output.append(function(alvo[i]))
    
    minIndex = output.index(min(output))







except ValueError:
    print('Sample size exceeded population size.')
            

xpoints = [i for i in range(epoch + 1)]


plt.plot(xpoints, historico)
plt.show()
import numpy as np
import random


class MultiLayerPerceptron:
    def __init__(self, input_layer_number = 1, hidden_layer_number = 3, output_layer_number = 1, learning_rate = 0.01, max_epoch = 10000, max_error = 1) -> None:
        
        #initiate parameters
        self.input_layer = input_layer_number       #neurons in input layer
        self.hidden_layer = hidden_layer_number     #neurons in hidden layer
        self.output_layer = output_layer_number     #neurons in output layer
        self.learning_rate = learning_rate          #learning rate
        self.max_epoch = max_epoch                  #maximum number of epoch
        self.max_error = max_error                  #maximum error accepted
        self.bias_neuron = -1

        self.WEIGHT_hidden = self.starting_weights(self.input_layer + 1,self.hidden_layer)
        self.WEIGHT_output = self.starting_weights(self.hidden_layer + 1, self.output_layer)

        self.input_layer_out = self.create_layer(self.input_layer + 1)
        self.hidden_layer_out = self.create_layer(self.hidden_layer + 1)
        self.output_layer_out = self.create_layer(self.output_layer)

        pass

    #starting weights
    def starting_weights(self, x, y ) -> list:
        #return [[random.random() - .5 for _ in range(x)] for __ in range(y)]
        return [[0 for _ in range(x)] for __ in range(y)]

    
    def create_layer(self, number) -> list:
        return [ 1 for _ in range(number) ]
    
    #activate function
    def f(self, x) -> float:
        return (2/(1 + np.exp(-x)) - 1)
    
    def df(self, x):
       return   (1 - self.f(x)**2  ) / 2
    


    def train(self, input_values,targets):

"""     def train(self, input_values,targets):

        input_length = len(input_values)
        last_err = 0
        curr_err = 0
        for epoch in range(0,self.max_epoch):
            error_list = []
           
            for i in range(0,input_length):
                out = self.predict(input_values[i])
                delta_out = []
                error_squared = (targets[i] - out[0])**2
                error_list.append(error_squared)
                
                #output layer
                for j in range(0,len(self.output_layer_out)):
                    net = np.dot(self.WEIGHT_output[j], self.hidden_layer_out)

                    for n in range(0,len(self.hidden_layer_out)):

                        delta = (targets[i] - out[j]) * self.df(net) 
                        delta_out.append(delta)
                        for k in range(0,len(self.hidden_layer_out)):
                            self.WEIGHT_output[j][k] +=  self.learning_rate * delta * self.hidden_layer_out[n]
                

                #hidden layer
                for l in range(0,len(self.WEIGHT_hidden)):

                    net = np.dot(self.WEIGHT_hidden[l], self.input_layer_out)
                    delta_in = 0

                    for n in range(0,len(delta_out)):
                        delta_in += delta_out[n] * self.WEIGHT_output[0][n]
                    
                    delta =  delta_in * self.df(net) 

                    for m in range(len(self.input_layer_out)):
                        self.WEIGHT_hidden[l][m] += self.learning_rate * delta * self.input_layer_out[0]
            
            epoch_error = sum(error_list)
            if epoch%1000 == 0:
                last_err = curr_err
                curr_err = epoch_error

                print(f"epoca: {epoch}\t erro da epoca: {epoch_error}\t delta_error: {curr_err - last_err}")
                print(f"weights hidden: {self.WEIGHT_hidden}")
                print(f"weights out: {self.WEIGHT_output}")
                print()
            if epoch_error <= self.max_error:
                break
 """
    #prediction function
    def predict(self, value) -> float:
        self.input_layer_out[0] = value
        
        #forward propagation
        #hidden layer
        for i in range(0,len(self.hidden_layer_out) - 1):
            net = np.dot(self.WEIGHT_hidden[i], self.input_layer_out).tolist()
            self.hidden_layer_out[i] =  self.f(net)
        
        #output layer
        for j in range(0,len(self.output_layer_out)):
            net = np.dot(self.WEIGHT_output[j], self.hidden_layer_out).tolist()
            self.output_layer_out[j] = self.f(net)

        return self.output_layer_out
    


if __name__ == "__main__":
    x = [ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    t = [-0.9602, -0.5770, -0.0729, 0.3771, 0.6405, 0.6600, 0.4609, 0.1336, -0.2013, -0.4344, -0.5000 ]

    rede = MultiLayerPerceptron()

    rede.train(x,t)
    err = []
    for i in range(len(x)):
        pred = rede.predict(x[i])
        err.append(abs(t[i] - pred[0]))
        print(f"x: {x[i]}\t t:{t[i]} predict: {pred[0]} delta: {err[i]}")
    print(f"erro total: {sum(err)}")
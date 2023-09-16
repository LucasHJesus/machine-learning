import pandas as pd
import random as rng
import graphs

class adaline:
    def __init__(self, learnin_rate:float = 0.001, max_error:float = 2, max_epoch:int = 100) -> None:
        self.learnin_rate:float = learnin_rate
        self.max_error:float = max_error
        self.max_epoch:int = max_epoch

    def __error__(self, target:int, y_in:float) -> float:
        return (target - y_in)*(target - y_in)
    
    def __activate_func__(self, value:float) -> int:
        return value
    
    def __round__(self,value:float) ->int:
        return 1 if value>=0 else -1
    
    def __update_weight__(self, old:float, target:int, x_in:float, y_in:int) -> float:
        return old + self.learnin_rate * (target - y_in) * x_in

    def __dot__(self, list1:list, list2:list)->float:
        list1_size:int=len(list1)
        list2_size:int=len(list2)
        dot:float = 0.0
        for i in range(min(list1_size,list2_size)):
            dot +=list1[i]*list2[i]
        dot += list2[-1] if list2_size > list1_size else list1[-1]
        return dot

    def training(self, file_name:str) -> None:

        training_set = pd.read_excel(file_name)
        self.weights = [(rng.random() - 0.5) for __ in range(len(training_set.columns)) ]
        error:float = self.max_error + 1.00
        columns:int = len(training_set.columns)
        rows:int =  len(training_set)
        target_column:int = columns - 1
        bias_column:int = -1
        epoch:int = 0
        sums:list =[]

        print("training started")

        while(error>self.max_error and epoch<self.max_epoch):
            errors:list = []

            for i in range(rows):
                row_list = training_set.loc[i, :].values.flatten().tolist()[0:-1]
                y_in:int = self.__dot__(list1 = self.weights, list2 = row_list )

                for j in range(columns - 1):
                    self.weights[j] = self.__update_weight__(old = self.weights[j], target = training_set.iat[i,target_column], x_in = training_set.iat[i,j],y_in=y_in)

                self.weights[bias_column] = self.__update_weight__(old = self.weights[bias_column], target = training_set.iat[i,target_column], x_in = 1,y_in=y_in)
                errors.append(self.__error__(target = training_set.iat[i,target_column] , y_in = y_in))
                
            epoch+=1
            error = sum(errors)
            print(f"epoca: {epoch}\tpesos: {self.weights}\terro: {error}")
            sums.append(error)
        graphs.errors(sums)


    def test(self,inputs:list) -> int:
            return self.__round__(self.__activate_func__(self.__dot__(inputs,self.weights)))

    def test_all(self, file_name:str) -> None:
            test_set = pd.read_excel(file_name)
            rows:int =  len(test_set)
            target_column:int = -1

            print("test started")

            for i in range(rows):
                row = test_set.loc[i, :].values.flatten().tolist()
                test_result = self.test(row[0:-1])
                print(f"inputs: {row[0:-1]}\t",end="")
                print(f"output: {test_result}\t",end="")
                print(f"target: {row[-1]}\t",end="")
                if int(test_result) == int(row[target_column]):
                    print(f"Passed")
                else:
                     print(f"Failed")
            
            graphs.dispersion(test_set,self.weights)


neuronio = adaline(max_epoch = 3000, learnin_rate = 0.001, max_error = 2)
neuronio.training("Basedados_B2.xlsx")
neuronio.test_all("Basedados_B2.xlsx")


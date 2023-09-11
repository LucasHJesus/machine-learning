import pandas as pd
import matplotlib.pyplot as plt
import random as rng


def __dot__(list1:list,list2:list):
    list1_size:int=len(list1)
    list2_size:int=len(list2)
    dot = 0
    for i in range(min(list1_size,list2_size)):
        dot +=list1[i]*list2[i]
    dot += list2[-1] if list2_size > list1_size else list1[-1]
    return dot

#print(__dot__(list1 = [4,5], list2 = [1,2,3]))



def line(coeficients:list, value:float)->float:
    return ( coeficients[1] * value ) / coeficients[0] + coeficients[2] 

table = pd.read_excel("Basedados_B2.xlsx",)
""" for i in range(len(table)):
    print(f"{i}\n{table.loc[i]}") if table.iat[i,2] == -1 else print("") """
#print(table)
weights:list = [-0.7194869890672786, -0.5769094885157631, 1.9228889413494898]


groups = table.groupby("t")

for name, group in groups:
    plt.plot(group.s1,group.s2, marker='o', linestyle='', markersize=12, label=name)
plt.legend()

""" print(f"({0},{line(weights,0)})")
print(f"({line(weights,0)}),{1})")
 """
plt.plot([0,line(weights,0)],[line(weights,1),1],color = "red")
plt.show() 






#row_list = table.loc[2, :].values.flatten().tolist()[0:-1]
#print(row_list)
#print(len(table.columns))
#index element of dataframe table.iat[0,1]
# list of random numbers [(rng.random() - 0.5) for __ in range(len(table.columns)) ]



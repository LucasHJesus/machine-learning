import matplotlib.pyplot as plt
import pandas as pd

def errors(error_list:list) ->None:
    plt.plot(error_list)
    plt.show()

def line(coeficients:list, value:float)->float:
    return ( coeficients[1] * value ) / coeficients[0] + coeficients[2]

def dispersion(dataframe:pd.core.frame.DataFrame,weights:list) -> None:
    
    groups = dataframe.groupby("t")
    for name, group in groups:
        plt.plot(group.s1,group.s2, marker='o', linestyle='', markersize=12, label=name)
    plt.legend()

    plt.plot([line(weights,0),0],[1,line(weights,1)],color = "red")
    plt.show() 


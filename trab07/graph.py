import matplotlib.pyplot as plt


def dots(x1,y1,x2,y2 ):
    plt.scatter(x1, y1, label = "dataset")
    plt.scatter(x2, y2, label = "predicted")
    

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("functions")

    plt.show()





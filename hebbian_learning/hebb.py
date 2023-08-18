
def step(value):
    if value >= 0:
        return True
    return False


def neuron(weight, A, B):
    return step(A*int(weight[0]) + B*int(weight[1]) + 1*int(weight[2]))

def modelMenu(weights):
    repeat = "Y"
    while(repeat == "Y"):
        A = int(input("insert A value(-1 for False, 1 for True)\t"))
        B = int(input("insert B value(-1 for False, 1 for True)\t"))
        result = neuron(weights,A,B)
        print("result: "+str(result))
        repeat = input("Repeat operation?[Y/n]")
    pass



def newWeight(oldWeight, x, y):
    return oldWeight + x * y

def hebb(input,bias, target):
    w1 = 0 
    w2 = 0
    b = 0

    for i in range(len(target)):
        w1 = newWeight(w1,input[i][0],target[i])
        w2 = newWeight(w2,input[i][1],target[i])
        b = newWeight(b,bias[i],target[i])
    
    return [w1,w2,b]



def operation(op):
    bias = [1,1,1,1]
    weight = []
    input = [   [-1,-1],
                [-1, 1],
                [ 1,-1],
                [ 1, 1]]
    
    target = [  [-1,-1,-1, 1], #and
                [-1, 1, 1, 1]] #or
    
    weight = hebb(input,bias, target[op])
    modelMenu(weight)
    


        
def menu():
    while(1):
        message = "insert operation number:\n\
                    0 And\n\
                    1 Or \n\
                    16 exit\n"
        op = int(input(message))
        if 16>=op and op>=0:
            return op

if __name__=="__main__":
    while(1):
        op = int(menu())
        if op == 16:
            break
        operation(op)
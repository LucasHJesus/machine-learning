#include <iostream>
#include <array> 


using namespace std;

enum outValues {
    F = -1,
    T = 1
};

outValues step(int op){
    if (op>0) return T;
    return F;
}

int newWeight(int oldWeight, int x, int y){
    return oldWeight + x * y;

}

array<int,3> train(array<array<outValues,2>,4> input, array<outValues,4> target){

    int w1 = 0, w2 = 0, b = 0;

    for(int i = 0; i < target.size(); i++){
        w1 = newWeight(w1,input[i][0],target[i]);
        w2 = newWeight(w2,input[i][1],target[i]);
        b = newWeight(b,1,target[i]);
    }

    return {w1,w2,b};
}

array<outValues,4> model(array<int,3> weight, array<array<outValues,2>,4> input){

    array<outValues,4> output;
    for(int i = 0; i<output.size();i++){
        output[i] = step(input[i][0] * weight[0] + input[i][1] * weight[1] + weight[2]);
    }

    return output;
}

array<array<outValues,3>,4> operation(int op){  
    array<outValues,4> output;

                                            //A  B
    array<array<outValues,2>,4> input = {{  {F,F},
                                            {F,T},
                                            {T,F},
                                            {T,T}}};
                                    
    array<array<outValues,4>,14> targets =  {{ 
                                        /*B  F,T,F,T
                                          A  F,F,T,T*/
                                            {F,F,T,T},//0  - id A
                                            {F,T,F,T},//1  - id B
                                            {F,F,F,T},//2  - A and B
                                            {F,T,F,F},//3  - !A and B
                                            {F,F,T,F},//4  - A and !B
                                            {T,T,T,F},//5  - A nand B
                                            {F,T,T,T},//6  - A or B
                                            {T,T,F,T},//7  - !A or B
                                            {T,F,T,T},//8  - A or !B
                                            {T,F,F,T},//9  - A nor B
                                            {T,F,T,F},//10 - !B
                                            {T,T,F,F},//11 - !A
                                            {F,F,F,F},//12 - y = 0
                                            {T,T,T,T},//13 - y = 1
                                      }};

    array<int,3> weight = train(input,targets[op]);
    array<array<outValues,3>,4> outMatrix;

    output = model(weight,input);

    outMatrix = assembleMatrix(input, output);
    
    return outMatrix;
}

array<array<outValues,3>,4> assembleMatrix(array<array<outValues,2>,4> input, array<outValues,4> output){
    array<array<outValues,3>,4> outMatrix;
    
    for(int i=0;i<output.size();i++){
        outMatrix[i][0] = input[i][0];
        outMatrix[i][1] = input[i][1];
        outMatrix[i][2] = output[i];
    }

    return outMatrix;
}

int menu(){
    int op;
    while(1){

        cout<<"insert operation number:\n"
            <<"0  - id A     \t"
            <<"1  - id B     \t"
            <<"2  - A and B  \t"
            <<"3  - !A and B \n"
            <<"4  - A and !B \t"
            <<"5  - A nand B \t"
            <<"6  - A or B   \t"
            <<"7  - !A or B  \n"
            <<"8  - A or !B  \t"
            <<"9  - A nor B  \t"
            <<"10 - !B       \t"
            <<"11 - !A       \n"
            <<"12 - y = 0    \t"
            <<"13 - y = 1    \t"
            <<"14 - exit     \n";
        cin>>op;

        if (op<=16 && op>=0) return op;
        
        cout<<"insert valid operation\n";

    }
    
}

void printMatrix(array<array<outValues,3>,4> matrix){
    cout<<"\n"
        <<"A\tB\tOUT\n";
    string a;
    for(int i = 0; i < matrix.size(); i++){
        for(int j = 0; j < matrix[0].size(); j++){
            matrix[i][j]==1?cout<<"T\t":cout<<"F\t";
        }
        cout<<"\n";
    }

    system("pause");

}
int main(){

    int op;
    array<array<outValues,3>,4> matrix;
    while (1)
    {
        op = menu();
        if (op>=14||op<0) break;
        matrix = operation(op);
        printMatrix(matrix);
    }

    return 0;
}
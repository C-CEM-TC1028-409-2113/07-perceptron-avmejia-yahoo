import math
# utiliza math.exp

def salida_neurona(l1,l2):
    if len(l1)!=len(l2):
        return "Error"
    else:
        long = len(l1)
        x=0.0;
        for i in range(long):
            x = x + l1[i]*l2[i] 
        sig = 1 / (1 + math.exp(-x))               
        return sig

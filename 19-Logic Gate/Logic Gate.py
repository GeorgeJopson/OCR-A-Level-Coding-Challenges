def boolToNumber(a):
    if(a==True):
        return 1
    else:
        return 0
def OR(a,b):
    if(a+b>=1):
        return 1
    else:
        return 0
def AND(a,b):
    if(a+b==2):
        return 1
    else:
        return 0
def XOR(a,b):
    if(a+b==1):
        return 1
    else:
        return 0
def NAND(a,b):
    return boolToNumber(not AND(a,b))
def NOR(a,b):
    return boolToNumber(not OR(a,b))
gates={
    "OR":OR,
    "AND":AND,
    "XOR":XOR,
    "NAND":NAND,
    "NOR":NOR
    }
gate=input("Input a logic gate:\nOR,AND,XOR,NAND,NOR\n")
a=int(input("Input 1 or 0:\n"))
b=int(input("Input 1 or 0:\n"))
print("Result="+str(gates.get(gate)(a,b)))

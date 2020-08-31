import cmath
def addComplex(complex1,complex2):
    return complex1+complex2
def subtractComplex(complex1,complex2):
    return complex1-complex2
def multiplyComplex(complex1, complex2):
    return complex1*complex2
def divideComplex(complex1,complex2):
    return complex1/complex2
print("1st number")
complex1=complex(int(input("Input the real part:")),int(input("Input the imaginary part:")))
print("2nd number")
complex2=complex(int(input("Input the real part:")),int(input("Input the imaginary part:")))
print(str(complex1)+"+"+str(complex2)+"="+str(addComplex(complex1,complex2)))
print(str(complex1)+"-"+str(complex2)+"="+str(subtractComplex(complex1,complex2)))
print(str(complex1)+"*"+str(complex2)+"="+str(multiplyComplex(complex1,complex2)))
print(str(complex1)+"/"+str(complex2)+"="+str(divideComplex(complex1,complex2)))

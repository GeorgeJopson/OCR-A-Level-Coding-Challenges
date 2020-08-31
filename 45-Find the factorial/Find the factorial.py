#Loop Solution
print("Loop Solution")
num=int(input("Input a number: "))
result=1
for i in range(num):
    result*=num-i
print(result)

#Recursion solution
print("Recursion Solution")
def factorial(num):
    if(num>1):
        result=num*factorial(num-1)
    else:
        result=1
    return result
print(factorial(int(input("Input a number: "))))

specialNums={
    3:"Fizz",
    5:"Buzz"
    }
def fizzBuzz(inputNum):
    export=""
    for number in list(specialNums.keys()):
        if(inputNum%number==0):
            export+=specialNums.get(number)
    return export if export!="" else str(inputNum)
fizzBuzzLength=int(input("What number do you want to go up to: "))
for num in range(1,fizzBuzzLength+1):
    print(fizzBuzz(num))
    

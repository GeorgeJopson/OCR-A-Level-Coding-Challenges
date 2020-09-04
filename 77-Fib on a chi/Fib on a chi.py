fibonacci=[1,1]
counter=2
currentNumber=1
while currentNumber<10**(1000-1):
    currentNumber=fibonacci[counter-2]+fibonacci[counter-1]
    fibonacci.append(currentNumber)
    counter+=1
print(counter)


def findNextPrime(startNum):
    possiblePrime=startNum+1
    while True:
        prime=True
        if(possiblePrime==0 or possiblePrime==1):
            prime=False
        else:
            for counter in range(2,possiblePrime):
                if(possiblePrime%counter==0):
                    prime=False
                    break
        if(prime):
            break
        else:
            possiblePrime+=1
    return possiblePrime
primes=[2,3,5]

inputNumber=int(input("Input number: "))
primeFactors=[]
while(inputNumber!=1):
    foundFactor=False
    for index in range(len(primes)):
        if(inputNumber%primes[index]==0):
            primeFactors.append(primes[index])
            inputNumber/=primes[index]
            foundFactor=True
    if(foundFactor==False):
        while (foundFactor==False):
            primes.append(findNextPrime(primes[-1]))
            if(inputNumber%primes[-1]==0):
                primeFactors.append(primes[-1])
                inputNumber/=primes[-1]
                foundFactor=True
print(primeFactors)

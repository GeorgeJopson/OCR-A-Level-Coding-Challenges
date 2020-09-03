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
def golbach(num):
    found=False
    while found==False:
        for currentPrime in primes:
            for otherPrime in primes:
                if(otherPrime+currentPrime==num and found==False):
                    print("{0}+{1}={2}".format(currentPrime,otherPrime,num))
                    found=True
        primes.append(findNextPrime(primes[-1]))
golbach(int(input("Input an even number greater than 2: ")))

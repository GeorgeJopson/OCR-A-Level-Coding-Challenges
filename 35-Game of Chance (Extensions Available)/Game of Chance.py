from random import randint
def isPrime(num):
    prime=True
    if(num==0 or num==1):
        prime=False
    else:
        for counter in range(2,num):
            if(num%counter==0):
                prime=False
                break
    return prime
betNum=int(input("Input a number from 0 to 30: "))
betAmount=int(input("Input an amount you want to bet: "))
payout=betAmount
if(betNum%2==0):
    payout*=2
if(betNum%10==0):
    payout*=3
if(isPrime(betNum)):
   payout*=5 
if(betNum<5):
    payout*=2
print("If you win, you'll get: "+str(payout))
randomNum=randint(0,30)
print("Your Number: "+str(betNum))
print("Number: "+str(randomNum))
if(betNum==randomNum):
    print("You win, you get: "+str(payout))
else:
    print("Oh wow, you lost.\nWho would have thought you lost a bet with a 3.23% chance of victory?\nAnyway you have now lost "+str(betAmount))

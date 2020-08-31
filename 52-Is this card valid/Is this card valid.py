#This is an exact copy of challenge 7 Credit Card Validator
cardNum=int(input("Input your 16 digit credit card:"))
cardList=[int(num) for num in str(cardNum)]
if(len(cardList)==16):
    checkSum=cardList[0:15]
    checkDigit=cardList[15]
    for index in range(len(checkSum)):
        if(index%2==0):
            checkSum[index]*=2
            if(checkSum[index]>=10):
                checkSum[index]=sum(map(lambda num:int(num),str(checkSum[index])))
    checkSum=sum(checkSum)
    if((checkSum+checkDigit)%10==0):
        print("Valid Card")
    else:
        print("Invalid Card")
else:
    print("Not 16 digits")

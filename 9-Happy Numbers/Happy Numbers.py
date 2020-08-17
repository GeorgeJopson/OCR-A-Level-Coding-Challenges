def isHappyNum(number):
    previousNums=[]
    while True:
        number=sum(map(lambda x:int(x)*int(x), str(number)))
        if(number in previousNums):
            return False
        if(number==1):
            return True
        previousNums.append(number)
happyNumList=[]
counter=0
while len(happyNumList)<8:
    if(isHappyNum(counter)):
        happyNumList.append(counter)
    counter+=1
print(happyNumList)

import math

def isKaprekar(num):
    squaredNum=str(num**2)
    left,right=math.floor(len(squaredNum)/2),math.ceil(len(squaredNum)/2)
    leftNum,rightNum=squaredNum[0:left],squaredNum[left:left+right]
    if leftNum=="": leftNum=0
    if rightNum=="": rightNum=0
    leftNum,rightNum= int(leftNum),int(rightNum)
    finalNumber=leftNum+rightNum
    if(num==finalNumber):
        return True
    else:
        return False
num=int(input("Input a number: "))

if(isKaprekar(num)):
    print(str(num)+" is a Kaprekar number")
else:
    print(str(num)+" is not a Kaprekar number")

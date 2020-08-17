from random import randint

def removeDuplicates(inputList):
    return list(set(inputList))

def repeatedValues(inputList):
    repeatedValues=[]
    for item in inputList:
        if(inputList.count(item)>1):
            repeatedValues.append(item)
    if(len(repeatedValues)==0):
        repeatedValues.append("None")
    return removeDuplicates(repeatedValues)
    
def makeRoll():
    possibleOutcomes=["Cherry" ,"Bell","Lemon","Orange","Star","Skull"]
    output=[possibleOutcomes[randint(0,len(possibleOutcomes)-1)] for symbol in range(3)]
    print(output)
    symbolGroupSize=4-len(removeDuplicates(output))
    outcomes={
        "1":{"Default":0},
        "2":{"Skull":-1,
             "Default":0.5},
        "3":{"Bell":5,
             "Skull":-money,
             "Default":3}
        }
    outcomesCategory = outcomes.get(str(symbolGroupSize))
    if(repeatedValues(output)[0] in outcomesCategory):
        return outcomesCategory.get(repeatedValues(output)[0])
    else:
        return outcomesCategory.get("Default")
money=1
while True:
    if(money<0):
        break
    print("You have £"+str(money))
    spin=input("Do you want a spin? yes/no")
    if(spin=="yes"):
        print("You pay £0.2 for a spin")
        money=round(money-0.2,2)
        print("You now have £"+str(money))
        moneyChange=makeRoll()
        if(moneyChange>=0):
            print("You won £"+str(moneyChange))
        else:
            print("You lost £"+str(-moneyChange))
        money=round(money+moneyChange,2)
        print("You now have £"+str(money))
    elif(spin=="no"):
        break
    
if(money>=0):
    print("You are left with £"+str(round(money,2)))
else:
    print("You owe £"+str(round(-money,2)))

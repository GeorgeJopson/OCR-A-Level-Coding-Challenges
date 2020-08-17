#Thief
pinNumbers = []
for x in range(4):
    pinNumbers.append(int(input('Enter a pin number')))

possibleCombinations=[]

combination=[0,0,0,0]


def noRepeats(inputList):
    if len(inputList) == len(set(inputList)):
        return True
    else:
        return False

for i in range(4**4):
        if noRepeats(combination):
            possibleCombinations.append([pinNumbers[combination[0]],pinNumbers[combination[1]],pinNumbers[combination[2]],pinNumbers[combination[3]]])
        combination[3]+=1
        for j in range(3,-1,-1):
            if combination[j] == 4:
                combination[j]=0
                combination[j-1]+=1

print(set(map(tuple,possibleCombinations)))

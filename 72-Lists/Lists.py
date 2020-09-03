from random import randint, choice
mainList=[]
#Integers in a range list
integers=[]
for num in range(int(input("Input a number: "))+1):
    integers.append(num)
mainList.append(integers)

#Insert item into a list
insertItemList=["Item "+str(num) for num in range(10)]
insertItemList.insert(int(input("Insert a number between 0 and {0}: ".format(str(len(insertItemList)-1)))),"Inserted Element")
mainList.append(insertItemList)

#Random selection list
bigList=[randint(0,100) for num in range(randint(0,100))]
randomList=[choice(bigList) for num in range(randint(0,15))]
mainList.append(randomList)

#Sort mainList
def insertionSort(inputList):
        for index in range(1,len(inputList)):
            currentItem=inputList[index]
            comparingItem=index-1
            while comparingItem>=0 and len(inputList[comparingItem])>len(currentItem):
                inputList[comparingItem+1]=inputList[comparingItem]
                comparingItem-=1
            inputList[comparingItem+1]=currentItem
        return inputList
mainList=insertionSort(mainList)
print(mainList)

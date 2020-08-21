inputList=[]
for num in range(10):
    inputList.append(input("Input a number: "))
newList=[[],[]]
for num in inputList:
    #The newList[1-num%2] sorts the numbers into 2 lists.
    #If it is an odd num%2=1 and then 1-1=0 so it goes in the first list
    #If it is even num%2=0 and then 1-1=1 so it goes in the second list
    newList[1-int(num)%2].append(int(num))
#This sorts the two lists in numericall order. I could have used newList[0].sort(key=int) and then newList[0].sort(key=int) but that would take 2 lines
newList=sorted(newList[0])+sorted(newList[1])
#This just converts every item into a string
newList=list(map(lambda x:str(x),newList))
#This joins everything together
print(",".join(inputList))
print(",".join(newList))

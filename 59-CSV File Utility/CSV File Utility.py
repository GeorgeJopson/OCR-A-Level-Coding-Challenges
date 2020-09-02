#Get data
csv=open("users.csv","r")
content=csv.readlines()
csv.close()
content=list(map(lambda line: line[:-1].split(","),content))
columnTitles=content[0]
content.pop(0)
def formatContent(line):
    lineDictionary={}
    for column in range(len(columnTitles)):
        lineDictionary[columnTitles[column]]=line[column]
    return lineDictionary
content=list(map(formatContent,content))
print("Unsorted File")
for user in content:
    print(user)
print("")
#Sort
def bubbleSort(inputList,targetCategory):
    swaps=True
    counter=0
    while swaps:
        swaps=False
        for index in range(len(inputList)-1-counter):
            if(inputList[index].get(targetCategory)>inputList[index+1].get(targetCategory)):
                temp=inputList[index]
                inputList[index]=inputList[index+1]
                inputList[index+1]=temp
                swaps=True
        counter+=1
    return inputList
def insertionSort(inputList, targetCategory):
        for index in range(1,len(inputList)):
            currentItem=inputList[index]
            comparingItem=index-1
            while comparingItem>=0 and inputList[comparingItem].get(targetCategory)>currentItem.get(targetCategory):
                inputList[comparingItem+1]=inputList[comparingItem]
                comparingItem-=1
            inputList[comparingItem+1]=currentItem
        return inputList
sortMethod=input("Which sort method do you want to use? (Bubble Sort/Insertion Sort)\n")
if(sortMethod=="Bubble Sort"):
    content=bubbleSort(content,"Age")
else:
    content=insertionSort(content,"Age")
print("Sorted File")
for user in content:
    print(user)
#Reformat Content to be put back into file and save back to file
def unFormatContent(lineDictionary):
    line=""
    for column in range(len(columnTitles)):
        line+=lineDictionary.get(columnTitles[column])
        if(column!=len(columnTitles)-1):
            line+=","
    line+="\n"
    return line
content=list(map(unFormatContent,content))
titleLine=",".join(columnTitles)+"\n"
content=titleLine+"".join(content)
csv=open("users.csv","w")
csv.write(content)
csv.close()
print("\nFile Saved")

inputs=[]
while True:
    userInput=input("Input a (one-letter) input name for the truth table or enter to make table\n")
    if(userInput==""):
        break
    else:
        inputs.append(userInput)
#Create table
possibilities=2**len(inputs)
table=[[] for i in range(possibilities)]
for columnIndex in range(len(inputs)):
    categorySize=len(table)/2**(columnIndex+1)
    counter=0
    for rowIndex in range(len(table)):
        counter+=1
        if(counter>categorySize):
            table[rowIndex].append("1")
        else:
            table[rowIndex].append("0")
        if(counter>=categorySize*2):
            counter=0
#Prep table for output
for line in table:
    line.extend(["|"," "])
inputs.extend(["|","Q"])
table.insert(0,inputs)
table.insert(1,["-"]*len(inputs))
for line in table:
    print(" ".join(line))


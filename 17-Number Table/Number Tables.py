#Special divide function to deal with when you divide by 0
def divide(x,y):
    if(y==0):
        return "N/A"
    else:
        return round(x/y,0)

#Operations dictionary
operations={
    "+":lambda x,y:x+y,
    "-":lambda x,y:x-y,
    "*":lambda x,y:x*y,
    "/":divide
    }

#Inputs from user
symbol=input("Input a symbol: ")
num=int(input("Input a number: "))

#Create table
table=[[] for line in range(num+1)]

#Do calculations
for column in range(0,num+1):
    for row in range(0,num+1):
        table[column].append(str(operations.get(symbol)(column,row)))

#Add extra elements to the table
table.insert(0,[symbol,"|"])
for number in range(num+1):
    table[0].append(str(number))
for column in range(0,num+1):
    table[column+1].insert(0,str(column))
    table[column+1].insert(1,"|")
table.insert(1,["-" for i in range(num+3)])

#Print Table
for line in table:
    print(" ".join(line))

from random import shuffle
from math import floor
def is0(num):
    if(num==0):
        return False
    else:
        return True
#Sudoku I used is the first one on https://www.memory-improvement-tips.com/printable-sudoku-puzzles-easy-1b.html
#The solution to the sudoku (proving the algorithm is correct) is on https://www.memory-improvement-tips.com/printable-sudoku-puzzles-easy-1b-solutions.html
def isValid(sudoku):
    for line in sudoku:
        line=list(filter(is0,line))
        if(len(line)!=len(list(set(line)))):
            return False
    for columnNum in range(9):
        column=[sudoku[line][columnNum] for line in range(9)]
        column=list(filter(is0,column))
        if(len(column)!=len(list(set(column)))):
            return False
    for box in range(9):
        startLine=floor(box/3)*3
        startColumn=box%3*3
        grid=[sudoku[startLine+floor(num/3)][startColumn+num%3] for num in range(9)]
        grid=list(filter(is0,grid))
        if(len(grid)!=len(list(set(grid)))):
            return False
    return True
def isCompleted(sudoku):
    full=True
    for num in range(9):
        if(any(item is 0 for item in sudoku[num])):
            full=False
    return (full and isValid(sudoku))
sudoku=[[0,9,6,      0,4,0,    0,3,0],
        [0,5,7,      8,2,0,       0,0,0],
        [1,0,0,   9,0,0,    5,0,0,],
        
        [0,0,9,   0,1,0,    0,0,8],
        [5,0,0,   0,0,      0,0,0,2],
        [4,0,0,   0,9,0,    6,0,0,],

        [0,0,4,       0,0,3,    0,0,1],
        [0,0,0,    0,7,9,       2,6,0],
        [0,2,0,       0,5,0,    9,8,0,]]

sudokuTemplate=[list(map(lambda item:0 if item==0 else "Number", line)) for line in sudoku]
counter=0
while(not isCompleted(sudoku)):
    if(sudokuTemplate[floor(counter/9)][counter%9]!="Number"):
        sudoku[floor(counter/9)][counter%9]=sudoku[floor(counter/9)][counter%9]+1
        if(isValid(sudoku)and sudoku[floor(counter/9)][counter%9]<=9):
            counter+=1
        elif(sudoku[floor(counter/9)][counter%9]>=9):
            sudoku[floor(counter/9)][counter%9]=0
            counter-=1
            while True:
                if(sudokuTemplate[floor(counter/9)][counter%9]=="Number"):
                    counter-=1
                else:
                    break
        

## Debbuging Lines (useful for seeing what is going on in the programme and having it work step by step)
##        for line in sudoku:
##            print(line)
##        print("")
##        temp=input("")
    else:
        counter+=1
for line in sudoku:
    print(line)

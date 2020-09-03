from random import randint
answer=[randint(1,9),randint(0,9),randint(0,9),randint(0,9)]
print(answer)
guessed=False
while guessed==False:
    guess=input("Input your 4 number guess: ")
    guess=list(map(lambda digit:int(digit),guess))
    mice=0
    men=0
    for digit in range(len(guess)):
        if(answer[digit]==guess[digit]):
            mice+=1
        else:
            men+=1
    if(mice==4):
        print("Correct the number was {0}! You win!".format("".join(list(map(lambda digit:str(digit),answer)))))
        break
    else:
        print("You have {0} mice and {1} men!".format(mice,men))

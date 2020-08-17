from random import randint,shuffle
class Question():
    def __init__(self,num1,num2,operationSymbol,operation):
        self.num1=num1
        self.num2=num2
        self.operationSymbol=operationSymbol
        self.answer=operation(num1,num2)
operations={
    "+": lambda x,y:x+y,
    "-": lambda x,y:x-y,
    "*": lambda x,y:x*y,
    "/": lambda x,y:x/y
    }
name=input("What is your name?\n")
score=0
questionOrder=["+","+","+","-","-","-","*","*","/","/"]
shuffle(questionOrder)
for question in questionOrder:
    while True:
        end=False
        try:
            newQuestion=Question(randint(0,10),randint(0,10),question,operations.get(question))
            if(isinstance(newQuestion.answer, int) or newQuestion.answer==round(newQuestion.answer,3)):
                end=True
        except:
            pass
        if(end==True):
            break
    studentAnswer=input(str(newQuestion.num1)+str(newQuestion.operationSymbol)+str(newQuestion.num2)+"=")
    try:
        studentAnswer=int(studentAnswer)
    except:
        studentAnswer=float(studentAnswer)
    if(studentAnswer==newQuestion.answer):
        print("Correct")
        score+=1
    else:
        print("Incorrect")
print('\n'+name+" your score was "+str(score)+"/"+str(len(questionOrder)))

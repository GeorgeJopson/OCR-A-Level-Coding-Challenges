#To Do List:
#Grab questions from file, stored in list
#Shuffle list and grab questions
from random import shuffle

#This section creates a shuffled list of the questions
f=open("questions.txt","r")
fileContents=f.readlines()
f.close()
def formatQuestions(fullQuestion):
    fullQuestion=fullQuestion.split("#")
    question=fullQuestion[0]
    answer=fullQuestion[1].split(",")
    answer[-1]=answer[-1].rstrip("\n")
    answer=list(map(lambda x:x.lower(), answer))
    return {"question":question,"answer":answer}
    
questionList=list(map(formatQuestions, fileContents))
shuffle(questionList)

#This section carries out the quiz
lengthOfQuiz=5
score=0
for questionNumber in range(lengthOfQuiz):
    currentTotalQuestion=questionList[questionNumber]
    currentQuestion=currentTotalQuestion.get("question")
    currentAnswer=currentTotalQuestion.get("answer")
    inputAnswer=input(currentQuestion+"\n")
    if(inputAnswer.lower() in currentAnswer):
        score+=1
        print("Correct")
    else:
        print("Incorrect, correct answers included: ")
        for answer in currentAnswer:
            print(answer.capitalize())
percentageScore=(score/lengthOfQuiz)*100
print("You scored %"+str(percentageScore))
if(percentageScore<50):
    print("Try harder")
elif(percentageScore>=50 and percentageScore<75):
    print("Good job but room for improvement")
else:
    print("Great job, well done.")

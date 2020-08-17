#Functions:

#Checks if the number plate is legal
def validNumberPlate(numberPlate):
    numberPlate=numberPlate.replace(' ','')
    if len(numberPlate)==7 and numberPlate[0:2].isalpha() and numberPlate[2:4].isdecimal() and numberPlate[4:7].isalpha():
        return 'Valid Number Plate'
    else:
        return 'Illegal Number Plate'

#Enters the second value of the start and end time + the distance
#Then it calculates the speed in mph
def speedCalculator(startTime,endTime,distance):
    timeTaken=(endTime-startTime)/60/60
    speed=distance/timeTaken
    return speed

#Opens up the file carDetails
#Then it splits up the file into a list
file=open('carDetails.txt','r')
cars=[]
for line in file:
    cars+=[line[:-1].split(',')]

#Constants
speedLimit=70

#Loop which checks and outputs all the data
counter=1
for vehicles in cars:
    #Checks the file
    print('Car '+str(counter)+':')
    #Checks whether the number plate is valid
    print(validNumberPlate(vehicles[0]))
    #Finds the speed
    speed=round(speedCalculator(int(vehicles[1]),int(vehicles[2]),1),0)
    #Outputs the speed
    print('Speed '+str(speed)+' mph')
    #Checks if it is over the speed limit
    if speed>speedLimit:
        print('Over Speed Limit')
    else:
        print('Under Speed Limit')
    #Adds a return
    print('\n')
    #Adds 1 to the counter
    counter+=1

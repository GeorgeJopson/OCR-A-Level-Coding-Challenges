from random import randint,choice
#Create dungeon
def availableExits(size,x,y):
    exits=["Up","Down","Left","Right"]
    if(x==0):
        exits.remove("Left")
    elif(x==size-1):
        exits.remove("Right")
    if(y==0):
        exits.remove("Up")
    return exits
class Room:
    def __init__(self,roomType,doors):
        self.roomType=roomType
        self.doors=doors
def addRoomExits(currentX,currentY,direction):
    dungeon[currentY][currentX].doors.append(direction)
    if(direction=="Left"):
        dungeon[currentY][currentX-1].doors.append("Right")
    elif(direction=="Right"):
        dungeon[currentY][currentX+1].doors.append("Left")
    elif(direction=="Down"):
        dungeon[currentY+1][currentX].doors.append("Up")
    else:
        dungeon[currentY-1][currentX].doors.append("Down")
size=4
dungeon=[[Room("ordinary",[]) for room in range(size)] for floor in range(size)]
currentX=randint(0,len(dungeon[0])-1)
currentY=0
[startX,startY]=[currentX,currentY]
direction=""
#Main Path
continueDungeon=True

while continueDungeon:
    down=False
    exits=availableExits(size,currentX,currentY)
    try:
        exits.remove("Up")
    except:
        pass
    #First floor
    if(direction==""):
        try:
            exits.remove("Down")
        except:
            pass
        direction=choice(exits)
        dungeon[currentY][currentX].roomType="path"
        addRoomExits(currentX,currentY,direction)
        if(direction=="Left"):
            currentX-=1
            
        else:
            currentX+=1
    else:
        dungeon[currentY][currentX].roomType="path"
        if(choice(exits)=="Down" or not("Left" in exits and "Right" in exits)):
            down=True
        else:
            addRoomExits(currentX,currentY,direction)
            if(direction=="Left"):
                currentX-=1
            else:
                currentX+=1
    #End of floor
    if(down):
        if(currentY==size-1):
            dungeon[currentY][currentX].roomType="end"
            continueDungeon=False
        else:
            addRoomExits(currentX,currentY,"Down")
            dungeon[currentY][currentX].roomType="path"
            currentY+=1
            direction=""
dungeon[startY][startX].roomType="start"
for floor in range(size):
    for room in range(size):
        if(dungeon[floor][room].roomType=="ordinary"):
            if(room==0):
                addRoomExits(room,floor,"Right")
            elif(room==size-1):
               addRoomExits(room,floor,"Left") 
            else:
                addRoomExits(room,floor,"Left")
                addRoomExits(room,floor,"Right")
for floor in range(size):
    for room in range(size):
        dungeon[floor][room].doors=list(set(dungeon[floor][room].doors))
[endX,endY]=[currentX,currentY]
#Adventure
##for floor in dungeon:
##    print(list(map(lambda room:room.roomType,floor)))
##print(" ")
##for floor in dungeon:
##    print(list(map(lambda room:room.doors,floor)))
print("You are an adventurer trying to find the lost artifact in an ancient temple.")

[playerY,playerX]=[startY,startX]
while True:
    roomType=dungeon[playerY][playerX].roomType
    exits=dungeon[playerY][playerX].doors
    if(roomType=="start"):
        print("You have just entered into the first room. On each floor their are {0} rooms and their are {0} floors".format(size))
    elif(roomType=="end"):
        print("You have entered the treasure room of the temple and have found the lost artifact.\nYour adventure ends here.")
        break
    else:
        print("You have entered the next room. You are on floor {0} and room {1}".format(playerY+1,playerX+1))
    print("There are the exits: ")
    for door in exits:
        print(door)
    move=input("Where do you want to go?\n")
    while not(move in exits):
        move=input("Where do you want to go?\n")
    if(move=="Left"):
        playerX-=1
    elif(move=="Right"):
        playerX+=1
    elif(move=="Down"):
        playerY+=1
    elif(move=="Up"):
        playerY-=1

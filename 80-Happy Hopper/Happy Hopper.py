def isHappyHopper(sequence):
    jumps=[]
    for number in range(len(sequence)-1):
        jumps.append(abs(sequence[number+1]-sequence[number]))
    requiredJumps=[]
    for number in range(1,len(sequence)):
        requiredJumps.append(number)
    jumps.sort()
    requiredJumps.sort()
    if(jumps==requiredJumps):
        return True
    else:
        return False
sequences=[[1,4,2,3],[7,8,1,100],[3,4,6,9,5]]
counter=1
for sequence in sequences:
    if(isHappyHopper(sequence)):
        print("Sequence {0} is a happy hopper!".format(counter))
    else:
        print("Sequence {0} is not a happy hopper.".format(counter))
    counter+=1

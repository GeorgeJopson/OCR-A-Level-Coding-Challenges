##Millions (Hundreds Tens Units) Thousands (Hundreds Tens Units)
unitNames=["one","two","three","four","five","six","seven","eight","nine"]
teenNames=["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tenNames=["ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
num=int(input("Input a number"))
numSave=num
numUnits=[]
for counter in range(1,8):
    units=(num%(10**counter))
    num-=units
    numUnits.insert(0,int(units/10**(counter-1)))
if(numSave==0):
    print("zero")
else:
    numName=[]
    if(numUnits[0]>0):
        numName.append(unitNames[numUnits[0]-1]+' million')
    if(numUnits[1]>0 or numUnits[2]>0 or numUnits[3]>0):
        if(numUnits[1]>0):
            numName.append(unitNames[numUnits[1]-1]+' hundred')
            if(numUnits[2]>0 or numUnits[3]>0):
                numName.append('and')
                if(numUnits[2]==1 and numUnits[3]>0):
                    numName.append(teenNames[numUnits[3]-1])
                else:
                    if(numUnits[2]>0):
                        numName.append(tenNames[numUnits[2]-1])
                    if(numUnits[3]>0):
                        numName.append(unitNames[numUnits[3]-1])
        numName.append('thousand')
    if(numUnits[4]>0):
        numName.append(unitNames[numUnits[4]-1]+' hundred')
        if(numUnits[5]>0 or numUnits[6]>0):
            numName.append('and')
    if(numUnits[5]==1 and numUnits[6]>0):
        numName.append(teenNames[numUnits[6]-1])
    else:
        if(numUnits[5]>0):
            numName.append(tenNames[numUnits[5]-1])
        if(numUnits[6]>0):
            numName.append(unitNames[numUnits[6]-1])
    print(' '.join(numName))

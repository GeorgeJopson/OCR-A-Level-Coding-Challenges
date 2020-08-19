def triangleType(triangle):
    if(len(set(triangle))==1):
        return "Equilateral"
    elif(len(set(triangle))==2):
        return "Isosceles"
    elif(triangle[0]**2+triangle[1]**2==triangle[2]**2):
        return "Right Angeled"
    else:
        return "Scalene"
    
triangle=[]
for side in range(1,4):
    triangle.append(input("Input side "+str(side)+": "))
triangle.sort(key=int)
triangle=list(map(lambda x:int(x),triangle))
if(triangle[0]+triangle[1]>triangle[2]):
    print("Valid Triangle")
    print("Triangle Type: "+triangleType(triangle))
    
else:
    print("Invalid Triangle")

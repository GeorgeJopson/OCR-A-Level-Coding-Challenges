def uniques(inputList):
    uniques=[]
    for item in inputList:
        tempList=inputList.copy()
        tempList.remove(item)
        if(not(item in tempList)):
            uniques.append(item)
    return uniques
#Example Lists
#Uniques are: butter,carrot,pepper,bread
weekA=["eggs","bacon","butter","carrot","pizza"]
weekB=["eggs","pepper","bread","bacon","pizza","pizza"]
overall=weekA+weekB
#Returns butter,carrot,pepper,bread so it is working
print(uniques(overall))

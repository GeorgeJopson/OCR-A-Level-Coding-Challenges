from random import shuffle
#Bubble sort function
def orderList(nums,ascending):
    swaps=True
    counter=0
    while swaps:
        swaps=False
        for index in range(len(nums)-1-counter):
            if(not(ascending or nums[index]>nums[index+1]) or (ascending and nums[index]>nums[index+1])):
                temp=nums[index]
                nums[index]=nums[index+1]
                nums[index+1]=temp
                swaps=True
        counter+=1
    return nums
#Set up for bubble sort function
nums=[]
for num in range(10):
    nums.append(int(input("Enter a number")))
ascendingOrDescending=input("Do you want the list to be in ascending order or descending order?(a/d) ")
if(ascendingOrDescending=="a"):
    ascending=True
else:
    ascending=False
#Output
print("Unordered list: "+str(nums))
print("Ordered List: "+str(orderList(nums,ascending)))

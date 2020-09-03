#I'm not sure what this challenge was asking for so this is what I think they meant,
#but it is likely I am wrong
members=9
expenses=[300,20,45,12,4,1,5,2,6,8,16,38,94]
totalExpenses=sum(expenses)
print("Each person should pay £{0:.2f}".format(totalExpenses/members))

#This challenge basically is asking for a list of character that appear in both
#strings x and y. This list should be called a

#This is because a permutation is a combination and we can have any permutation
#and therefore combination of a to match the subsequence of x or y

#A subsequence a list where order does matter but you can delete as many items
#as needed. However we don't need to worry about order as the list a can
#be in any order to match the list x or y which needs to be in a specific order.

#We can't take items out of a (as it isn't a subsequence), so all the items in a need to be in x and y.

#Therefore the largest list a could be is a list of all the letters shared
#between x and y.
#The hard thing about this challenge is understanding what it is asking and not the actual program,
#that being said I may have misunderstood the challenge and this might all be wrong so ¯\_(ツ)_/¯
x=input("Input a string: ")
y=input("Input another string: ")
a=""
for xLetter in x:
    if(xLetter in y):
        a+=xLetter
print(a)

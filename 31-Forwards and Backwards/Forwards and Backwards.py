#NOTE: This is an exact duplicate of the palindromes challenge (number 20)
from math import floor
word=input("Input a word:\n").lower()
palindrome=True
for letter in range(floor(len(word)/2)):
    if(word[letter]!=word[-(letter+1)]):
        palindrome=False
statement="is" if palindrome==True else "is not"
print(word.capitalize()+" "+statement+" a palindrome.")

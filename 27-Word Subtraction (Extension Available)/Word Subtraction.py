word1=input("Input a word: ")
word2=input("Input a word: ")
word1ASCII=int("".join([str(ord(letter)) for letter in word1]))
word2ASCII=int("".join([str(ord(letter)) for letter in word2]))
output=word1ASCII-word2ASCII
print(word1+"-"+word2+"="+str(output))

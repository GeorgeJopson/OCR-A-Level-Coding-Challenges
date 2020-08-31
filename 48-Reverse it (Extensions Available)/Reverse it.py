word=input("Input your word: ")
reverse=''
for letter in range(len(word),0,-1):
    reverse+=word[letter-1]
print(reverse)

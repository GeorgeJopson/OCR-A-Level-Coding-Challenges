#NOTE: This is an exact copy of the Ceaser Cipher challenge task (number 13)
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encodeOrDecode(letter,task):
    index=alphabet.index(letter.lower())
    if(letter==' '):
        return ' '
    else:
        if(task=="e"):
            encodedIndex=index+key
        else:
            encodedIndex=index-key
        while encodedIndex>25:
            encodedIndex-=26
        while encodedIndex<0:
            encodedIndex+=26
        if (letter==letter.lower()):
            return alphabet[encodedIndex]
        else:
            return alphabet[encodedIndex].upper()
    
key=int(input("Input the key: "))
userInput=input("Input message:")
task=input("Do you want to encode or decode? (e/d)")
export=''
for letter in userInput:
    export+=encodeOrDecode(letter,task)
print(export)

#Vignere Cipher
def encodeOrDecode(letter,task,key):
    if(letter==' '):
        return ' '
    else:
        index=alphabet.index(letter.lower())
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
#Alphabet
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#Inputs
message=input("Input your message: ")
key=input("Input your key: ")
task=input("Do you want to encode or decode? (e/d): ")
#Message
message=[letter for letter in message]
#Keystream
keystream=[]
counter=0
while len(keystream)!=len(message):
    keystream.append(alphabet.index(key[counter]))
    counter+=1
    if(counter>=len(key)):
        counter=0
#Encrypt
export=""
for letter in range(len(message)):
    export+=encodeOrDecode(message[letter],task,keystream[letter])
print(export)
    

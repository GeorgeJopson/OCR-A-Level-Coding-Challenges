def isPangram(string):
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for letter in string:
        try:
            del alphabet[alphabet.index(letter.lower())]
        except:
            pass
    if(len(alphabet)==0):
        return True
    else:
        return False
if(isPangram(input("Input a string: "))):
    print("It is a pangram")
else:
    print("It is not a pangram")


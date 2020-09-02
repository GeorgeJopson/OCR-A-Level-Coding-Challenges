from random import choice,randint
characters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","!","£","$","%","^","&","*","(",")","-","_","+","=","{","}","[","]",":",";","@","~","#"," "]
length=int(input("How long do you want your password to be? (Recommended atleast 10 characters)\n"))
password=""
for index in range(length):
    character=choice(characters)
    if(character.isalpha()):
        if(randint(0,1)==1):
            character=character.upper()
    password+=character
print(password)

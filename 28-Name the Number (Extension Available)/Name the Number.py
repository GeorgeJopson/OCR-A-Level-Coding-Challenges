key={
    "2":["a","b","c"],
    "3":["d","e","f"],
    "4":["g","h","i"],
    "5":["j","k","l"],
    "6":["m","n","o"],
    "7":["p","q","r","s"],
    "8":["t","u","v"],
    "9":["w","x","y","z"]
    }
phoneNum=input("Input you phone num: ")
endPhoneNum=""
for character in phoneNum:
    if(character.isdigit()):
        endPhoneNum+=character
    else:
        for num in list(key.keys()):
            if((character.lower() in key.get(num)) or (character.upper() in key.get(num))):
                endPhoneNum+=str(num)
print(endPhoneNum)

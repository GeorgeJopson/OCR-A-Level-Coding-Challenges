from time import sleep
signals={
    "a":"/|\n |",
    "b":"-|\n |",
    "c":"\|\n |",
    "d":"| \n||\n |",
    "e":"|/\n| ",
    "f":"|-\n| ",
    "g":"|\ \n  \\",
    "h":"-/\n/",
    "i":"\  \n \/\n /",
    "j":"|\n|-",
    "k":"  |\n /|\n/",
    "l":"   /\n // \n/",
    "m":" /-\n/",
    "n":"/\\",
    "o":"\ \n-\\",
    "p":" |\n-|",
    "q":"  /\n-/",
    "r":"--",
    "s":"-\\\n  \\",
    "t":"\ |\n \|",
    "u":"\  /\n \/",
    "v":"|\n|\\\n  \\",
    "w":" /\n/-",
    "x":" /\n/\\\n  \\",
    "y":"\\\n \-",
    "z":"\-\n \\",
    "space":"||\n||"
    }
def clear():
    print("\n"*40)
message=input("Input a message")
message=list(map(lambda character:character.lower(), message))
for letter in message:
    clear()
    if(letter==" "):
        print(signals.get("space"))
    else:
        print(signals.get(letter))
    sleep(1)

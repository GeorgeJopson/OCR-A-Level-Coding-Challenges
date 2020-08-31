textSpeak={
    "rofl":"rolling on the floor laughing",
    "lol":"laugh out loud",
    "stfu":"shut the flip up",
    "wap":"nope, not doing that one",
    "yolo":"you only live once"
    }
def convert(word):
    if word.lower() in textSpeak:
        return textSpeak.get(word.lower())
    else:
        return word
message=input("Input the message with text speak in:\n")
message=message.split()
message=list(map(convert,message))
print(" ".join(message))

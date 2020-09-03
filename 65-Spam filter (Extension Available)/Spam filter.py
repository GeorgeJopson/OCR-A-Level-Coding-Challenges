menu=["fish and chips","eggs","sausages","pasta","curry","stirfry"]
menu=list(map(lambda dish:dish+" + spam",menu))
for dish in menu:
    print(dish)

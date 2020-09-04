#This is a super slow method of doing this but it works so this is a win for me.
total=2.5
coins=[2,1,0.5,0.2,0.05,0.02,0.01]
combinations=[]
for twoPound in range(int(total/2)+1):
    for onePound in range(int(total/1)+1):
        for fiftyPee in range(int(total/0.5)+1):
            print("Processing...")
            for twentyPee in range(int(total/0.2)+1):
                for fivePee in range(int(total/0.05)+1):
                    for twoPee in range(int(total/0.02)+1):
                        for onePee in range(int(total/0.01)+1):
                            if(twoPound*2+onePound*1+fiftyPee*0.5+twentyPee*0.2+fivePee*0.05+twoPee*0.02+onePee*0.01==total):
                                combinations.append([twoPound,onePound,fiftyPee,twentyPee,fivePee,twoPee,onePee])
print("Finished calculation\n\n")
for combination in combinations:
    print(combination)

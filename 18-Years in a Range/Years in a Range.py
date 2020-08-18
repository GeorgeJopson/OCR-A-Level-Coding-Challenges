def repeatedDigit(year):
    year=list(str(year))
    yearNoRepeats=list(set(year))
    if(len(year)!=len(yearNoRepeats)):
        return True
    else:
        return False
startNum=2000
endNum=2100
yearsRepeatedDigit=0
for number in range(startNum,endNum+1):
    if(repeatedDigit(number)):
        print(str(number)+" has a repeated digit")
        yearsRepeatedDigit+=1
    else:
        print(str(number)+" does not have a repeated digit")
plural="" if yearsRepeatedDigit==0 else "s"
print("From "+str(startNum)+" and "+str(endNum)+"(inclusive)there are "+str(yearsRepeatedDigit)+" number"+plural +" with a repeated digit.")

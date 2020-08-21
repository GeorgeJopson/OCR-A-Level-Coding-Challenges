alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num=int(input("Input a denary number:"))
base=int(input("Input a base to convert to (no less than 2 and no greater than 62):"))
while(base<2 or base>62):
    base=int(input("Input a base to convert to (no less than 2 and no greater than 62):"))
converted=[]
counter=0
if(num==0):
    print("0")
else:
    while num!=0:
        digit=int((num%base**(counter+1))/(base**counter))
        if digit>9:
            if(digit>35):
                digit=alphabet[digit-36].lower()
            else:
                digit=alphabet[digit-10]
        converted.insert(0,str(digit))
        num-=int(num%base**(counter+1))
        counter+=1
print("".join(converted))


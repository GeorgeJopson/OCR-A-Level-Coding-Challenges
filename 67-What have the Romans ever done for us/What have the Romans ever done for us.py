class Numeral:
    def __init__(self,symbol,number):
        self.symbol=symbol
        self.number=number
numerals=[Numeral("I",1),Numeral("V",5),Numeral("X",10),Numeral("L",50),Numeral("C",100),Numeral("D",500),Numeral("M",1000)]
num=int(input("Input a number (up to 999): "))
digits=[]
length=len(str(num))
for place in range(length):
    digits.append(int(str(num)[place])*10**(length-place-1))
roman=""
for digit in digits:
    start=0
    while True:
        if(numerals[start+1].number<=digit):
            start+=1
        else:
            break
    subtractive=False
    for numeral in range(start,-1,-1):
        if(numerals[numeral].number+digit==numerals[start+1].number):
            subtractive=True
            minusNum=numerals[numeral].symbol
    if(subtractive):
        roman+=minusNum
        roman+=numerals[start+1].symbol
    else:
        for numeral in range(start,-1,-1):
                quantity=int(digit/numerals[numeral].number)
                digit-=quantity*numerals[numeral].number
                roman+=numerals[numeral].symbol*quantity
print(roman)

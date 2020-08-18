def timesTables():
    x=int(input("Input a number:"))
    y=int(input("Input a second number:"))
    print(str(x)+"x"+str(y)+"="+str(x*y))
def VAT():
    normalPrice=float(input("Input the price without VAT:"))
    print("The price with VAT is £"+str(round(normalPrice*1.2,2)))
def BMI():
    mass=int(input("Input your mass in kg:"))
    height=int(input("Input your height in m:"))
    print("Your BMI is "+str(mass/(height**2)))
    
calculators={
    "Times Tables":timesTables,
    "VAT":VAT,
    "BMI":BMI
    }
print("The available calculators are:")
for calculator in list(calculators.keys()):
    print(calculator)
calculators.get(input("Choose a calculator:"))()

#Mortgage amount
mortgage=int(input("Input the mortgage amount: "))
#Number of years
years=int(input("Input how long you have to pay off the £{0:d} mortgage: ".format(mortgage)))
#Interest
interest=float(input("What is the interest: "))

months=years*12
interestMultiplier=interest/100
interestMultiplierPerMonth=interestMultiplier/12
mortgagePayment= mortgage*(interestMultiplierPerMonth*(1+interestMultiplierPerMonth)**months)/((1+interestMultiplierPerMonth)**months-1)
print("Monthly Payment: £{0:.2f}".format(mortgagePayment))

width=float(input("Input the width of your floor in meters: "))
height=float(input("Input the height of your floor in meters: "))
area=width*height
costPerMeterSquared=25
cost=area*costPerMeterSquared
print("The cost to cover it in tiles (£25 for 1 metter squared is): £"+str(cost))

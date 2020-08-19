import datetime
def isLeapYear(year):
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                return True
        else:
            return True
    return False
def february():
    if(isLeapYear(int(year))):
        return 29
    else:
        return 28
day=int(input("What is the day: "))
month=int(input("What is the month: "))
year=int(input("What is the year: "))
#This bit makes the month dictionary. I know I could have written it out
#manualy but I couldn't be bothered so you get all this fun code.
monthLength={
    }
dayName={
    0:"Monday",
    1:"Tuesday",
    2:"Wednesday",
    3:"Thursday",
    4:"Friday",
    5:"Saturday",
    6:"Sunday"
    }
counter=0
for monthNum in range(1,13):
    counter+=1
    monthLength[monthNum]= 30 if counter%2==0 else 31
    if(counter>=7):
        counter=0
monthLength[2]= 29 if isLeapYear(year) else 28
if(day<=monthLength.get(month)):
    print("Valid Date")
    print("Today is a "+dayName.get(datetime.datetime(year,month,day).weekday()))
else:
    print("Invalid Date")


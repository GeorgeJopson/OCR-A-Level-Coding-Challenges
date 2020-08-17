conversions = {
    "Celsius":{
        "Celsius":lambda inputTemp:inputTemp,
        "Fahrenheit":lambda inputTemp:(inputTemp*9/5)+32,
        "Kelvin":lambda inputTemp:inputTemp+273.15
        },
    "Fahrenheit":{
        "Fahrenheit": lambda inputTemp:inputTemp,
        "Celsius":lambda inputTemp:(inputTemp-32)*5/9,
        "Kelvin":lambda inputTemp:(inputTemp-32)*5/9+273.15
        },
    "Kelvin":{
        "Kelvin": lambda inputTemp:inputTemp,
        "Celsius": lambda inputTemp:inputTemp-273.15,
        "Fahrenheit": lambda inputTemp:(inputTemp-2731.5)*9/5+32
        }
    }
inputUnit = input("What is the temperature you are starting in? Celsius/Fahrenheit/Kelvin")
inputUnitValue =int(input("What is the value of the starting temp?"))
convertToUnit = input("What is the temperature you are ending in? Celsius/Fahrenheit/Kelvin")
print("Your converted value is " + str(conversions.get(inputUnit).get(convertToUnit)(inputUnitValue)))

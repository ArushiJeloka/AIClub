#pairs_of_shoes = int(input("How many pairs of shoes do you have? "))

def awordin(gasoline):
    if(20 < gasoline < 100):
        liters = gasoline * 3.7854
        liters = round(liters, 4)
        print(liters, " liters of gasoline")

        barrels = round(gasoline/19.5, 3)
        print(barrels, " barrels of oil")

        price = gasoline * 3.65
        round(price, 2)
        print(price, " dollars")

    elif(gasoline < 20):
        return "Less than 20"

    else:
        return "Too many gallons"

gasoline = int(input("How many gallons of gasoline do you have? "))
print(awordin(gasoline))
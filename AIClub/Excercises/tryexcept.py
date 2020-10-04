#Try and except functions are used to try something on data and if it does not work, the except directs the program on how to move forward

x = input("Enter number: ") #here, a string input is being taken from the user

try:                                        #this code tries to convert the string input to a float
    print(" Your number was: ", float(x))

except:                                     #if the input is not a number, it outputs the error message
    print("Error: number was not entered")

#Use try and except to make a two number input calculator which outputs an error if anything besides the numbers/calculation functions is entered
'''make a basic four function calculator with 2 numbers on which operations will be performed'''

one = float(input("Enter first value : "))
two = float(input("Enter second value : "))
operation = int(input("Enter operation type - 1: ADD, 2: SUBTRACT, 3: MULTIPLY, 4: DIVIDE   "))


if operation == 1:
    print(one + two)

if operation == 2:
    print(one - two)

if operation == 3:
    print(one * two)

if operation == 4:
    print(one / two)
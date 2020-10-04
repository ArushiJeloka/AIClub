'''Write a code for the three ideal gases of P/T, PV, V/T with user input. The user should be able to enter decimal values.
Aditionally, include the option of doing another calculation and if the user responds with "no", exit the code'''


import sys
n = 0

while n >= 0:
    if n > 0:
        l = input("another calculation? type yes or no: ")
        if l == 'no':
            sys.exit()
        elif l == 'yes':
            x = input("Unkown variable: ")
            y = input("Known variable: ")
            if x == 'p' and y == 'v':
                vone = float(input("Initial volume: "))
                pone = float(input("Inital Pressure: "))
                vfinal = float(input("Final Volume: "))
                print("final pressure: ")
                print(vone*pone/vfinal)
            if x == 'v' and y == 'p':
                vone = float(input("Initial volume: "))
                pone = float(input("Inital Pressure: "))
                pfinal = float(input("Final Pressure: "))
                print("final pressure: ")
                print(vone * pone / pfinal)

            if x == 'v' and y == 't':
                vone = float(input("Initial volume: "))
                tone = float(input("Inital temperature: "))
                tfinal = float(input("Final temperature: "))
                print("final volume: " )
                print(vone / tone * tfinal)

            if x == 'p' and y == 't':
                pone = float(input("Initial pressure: "))
                tone = float(input("Inital temperature: "))
                tfinal = float(input("Final temperature: "))
                print("final pressure: ")
                print(pone / tone * tfinal)

            if x == 't' and y == 'p':
                pone = float(input("Initial pressure: "))
                tone = float(input("Inital temperature: "))
                pfinal = float(input("Final pressure: "))
                print("final temperature: ")
                print(pfinal / pone / tone)

            if x == 't' and y == 'v':
                vone = float(input("Initial volume: "))
                tone = float(input("Inital temperature: "))
                vfinal = float(input("Final volume: "))
                print("final temperature: ")
                print(vfinal / vone / tone)

            n =+ 1

    if n == 0:
            print("p: pressure, v: volume, t: temperature")
            x = input("Unkown variable: ")
            y = input("Known variable: ")
            if x == 'p' and y == 'v':
                vone = float(input("Initial volume: "))
                pone = float(input("Inital Pressure: "))
                vfinal = float(input("Final Volume: "))
                print("final pressure: ")
                print(vone*pone/vfinal)
            if x == 'v' and y == 'p':
                vone = float(input("Initial volume: "))
                pone = float(input("Inital Pressure: "))
                pfinal = float(input("Final Pressure: "))
                print("final pressure: ")
                print(vone * pone / pfinal)

            if x == 'v' and y == 't':
                vone = float(input("Initial volume: "))
                tone = float(input("Inital temperature: "))
                tfinal = float(input("Final temperature: "))
                print("final volume: " )
                print(vone / tone * tfinal)

            if x == 'p' and y == 't':
                pone = float(input("Initial pressure: "))
                tone = float(input("Inital temperature: "))
                tfinal = float(input("Final temperature: "))
                print("final pressure: ")
                print(pone / tone * tfinal)

            if x == 't' and y == 'p':
                pone = float(input("Initial pressure: "))
                tone = float(input("Inital temperature: "))
                pfinal = float(input("Final pressure: "))
                print("final temperature: ")
                print(pfinal / pone / tone)

            if x == 't' and y == 'v':
                vone = float(input("Initial volume: "))
                tone = float(input("Inital temperature: "))
                vfinal = float(input("Final volume: "))
                print("final temperature: ")
                print(vfinal / vone / tone)
            n =+ 1
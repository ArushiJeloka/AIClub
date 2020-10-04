'''Make a user input PV=nRT calculator'''

r = float(.08206)
miss = int(input("Missing Variable? (1 = p, 2 = v, 3 = n, 4 = t): "))

if miss == 1:
    v = float(input("Volume(L): "))
    n = float(input("Moles: "))
    t = float(input("Temperature(k): "))
    print((n*r*t)/v)
elif miss == 2:
    p = float(input("Pressure(atm): "))
    n = float(input("Moles: "))
    t = float(input("Temperature(k): "))
    print((n*r*t)/p)
elif miss == 3:
    p = float(input("Pressure(atm): "))
    v = float(input("Volume(L): "))
    t = float(input("Temperature(k): "))
    print((p*v)/(r*t))
elif miss == 4:
    p = float(input("Pressure(atm): "))
    v = float(input("Volume(L): "))
    n = float(input("Moles: "))
    print((p*v)/(r*n))



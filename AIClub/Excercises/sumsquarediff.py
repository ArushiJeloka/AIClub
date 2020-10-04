sumofsquares = 0
squareofsums = 0
z = 0
for x in range(101):
    y = x * x
    sumofsquares = sumofsquares + y
    z += x
    squareofsums = z**2
print(squareofsums - sumofsquares)

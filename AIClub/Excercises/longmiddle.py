def lg(a, b):
    if(len(a) > len(b)):
        return b + a + b
    else:
        return a + b + a

print(lg('cat', 'labyrinth'))
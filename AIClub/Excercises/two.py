'''if the word is larger than 2 characters long, print the first two and last 2 letters of the word'''
def print_both_ends(str):
    if len(str) < 2:
        return ' '
    return str[0:2] + str[-2:]

straw = "turtles"

print(print_both_ends(straw))

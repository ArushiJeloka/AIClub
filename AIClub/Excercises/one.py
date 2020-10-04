'''Print the number of times each letter in a string appears'''


one = "Hi I am hungry"
two = "Python is superior to Java"

def char_frequency(one):
    dict = {}
    for n in one:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1

    return dict

print(char_frequency(two))
'''print the longest word from a list of words'''

def length_longest(str):
    word = []
    for n in str:
        word.append((len(n), n))
    word.sort()
    return word[-1][1]

print(length_longest(["Hello", "Dinasour", "Fun", "WhyamIdoingthisat12am?"]))
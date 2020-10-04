'''Add 'ing' to the end of every word which is 3 characters or longer. If the word already ends in 'ing', add 'ly' to the end
 If the word is less than 3 characters long, return ' ' '''

def adding_ing(str):
    if len(str) < 3:
        return ' '

    elif str[-3:] == 'ing':
        return str + 'ly'

    return(str + 'ing')

string = 'bowling'
stringone = 'play'
stringtwo = 'hi'

print(adding_ing(string))





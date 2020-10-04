'''Get the first letter of the word and replace every mention of that letter, except the initial, with a dollar sign'''
def change_first(str):
    n = str[0]
    str = str.replace(n, '$')
    str = n + str[1:]
    return str

stre = 'batban'

print(change_first(stre))



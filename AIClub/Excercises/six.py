'''replace every mention of 'not poor' in a string with 'good' '''

def not_poor(str):
    rnot = str.find('not')
    rpoor = str.find('poor')

    if rpoor > rnot and rpoor > 0 and rnot > 0:
        str = str.replace(str[rnot:(rpoor+4)], 'good')
        return str
    else:
        return str

hi = 'this is not not poor'
print(not_poor(hi))
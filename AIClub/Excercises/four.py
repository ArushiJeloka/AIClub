'''Switch the first letter of both the strings'''

def join_strings(a, b):

    strfour = b[0] + a[1:] + ' ' + a[0] + b[1:]
    return(strfour)

print(join_strings('abc', 'xyz'))
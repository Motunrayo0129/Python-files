def rotate(a, b, c):
    return(c, b, a)

a, b, c = 'Doug', 22, 1984
print(rotate(a, b, c))

a, b, c  = rotate(a, b, c)
print(a, b, c)

a, b, c = rotate(a, b, c)
print(a, b, c)


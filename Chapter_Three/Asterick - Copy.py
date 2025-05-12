rows = 10

for i in range(1, rows + 1):
    # Pattern A: Left-aligned increasing
    for j in range(i):
        print('*', end='')
    print(' ' * (rows - i), end='  ')  

    # Pattern B: Left-aligned decreasing
    for j in range(rows - i + 1):
        print('*', end='')
    print(' ' * (i - 1), end='  ')  

    # Pattern C: Right-aligned decreasing
    print(' ' * (i - 1), end='')     
    for j in range(rows - i + 1):
        print('*', end='')
    print('  ', end='')            

    # Pattern D: Right-aligned increasing
    print(' ' * (rows - i), end='') 
    for j in range(i):
        print('*', end='')

    print()
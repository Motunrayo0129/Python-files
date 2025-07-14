for num in range(1, 11):
    for _ in range(0, num):
        print('*', end='')
    print()
print()

for num in range(10, 0, -1):
    for _ in range(0, num):
        print('*', end='')
    print()
print()

for num in range(10, 0, -1):
    for _ in range(0 - num):
        print(' ', end='')

    for _ in range(0, num):
        print('*', end='')
    print()
print()

for num in range(1, 11):
    for _ in range(10 - num):
        print(' ', end='')


    for _ in range(num):
        print('*', end='')
    print()

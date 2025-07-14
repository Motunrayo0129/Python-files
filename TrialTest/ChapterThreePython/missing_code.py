for row in range(1, 11):
    for col in range(1, 11):
        print('<' if row % 2 == 1 else '>', end='')
    print()

for row in range(2):
    for col in range(7):
        print('@', end='')
    print()
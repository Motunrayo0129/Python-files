for i in range(2):
    value = int(input('Enter an integer (-1 to break): '))

    if value == -1:
        break

    else:
        print('The loop terminated without executing the break')

print('You entered:', value)
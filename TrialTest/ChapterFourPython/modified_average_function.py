def get_average(*args):
    count = 0
    total = 0
    average = 0
    for number in args:
        total += number
        count += 1
        average = total / count
    return f"{average:.2f}"


print(get_average(15, 12, 13))
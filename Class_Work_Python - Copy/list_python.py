import random
number = random.randint(1, 11)

my_list = []
print(my_list)
def length_of_list():
    number = random.randint(1, 50)
    for i in range(10):
        my_list.append(random.randint(1, 50))
length_of_list()
print(my_list)

def sum_of_even_position():
    counter = 0
    index = 0
    for number in my_list:
        if index % 2 == 0:
            counter += my_list[index]
        index += 1
    return counter
print(sum_of_even_position())

def sum_of_odd_position():
    counter = 0
    index = 0
    for number in my_list:
        if index % 2 == 1:
            counter += my_list[index]
        index += 1
    return counter
print(sum_of_odd_position())


def multiply_every_third_position():
    count = 1
    for number in range(1, list_number, 3):
        return number * count



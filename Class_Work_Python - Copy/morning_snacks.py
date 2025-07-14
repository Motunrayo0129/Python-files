def return_element_three(numbers):
    number = []
    numbers.append(number)
    return numbers[2]

num = return_element_three([10, 20, 30, 40, 50])
print(num)
print("=" * 50)

def replaced_colors(color, exchange):
    color = list(color)
    color[2] = exchange
    return color

print(replaced_colors(['red', 'green', 'blue'], 'white'))
print("=" * 50)
def remove_colors(color, exchange):
    color = list(color)
    color.remove(exchange)
    return color

print(remove_colors(['red', 'green', 'blue'], 'blue'))
print("=" * 50)

def numbers_to_remove(numbers, exit_number):
    number = []
    numbers.remove(exit_number)
    return numbers

print(numbers_to_remove([10, 20, 30, 40, 50], 40))
print("=" * 50)

def length_of_names(names):
    names = list(names)
names = ['Alice', 'Bob', 'Charlie']
print(len(names[0]))
print(len(names[1]))
print(len(names[2]))
print("=" * 50)

ascending_numbers = [8, 9, 7, 4, 6, 5]
sorted_ascending_numbers = sorted(ascending_numbers)
print(sorted_asscending_numbers)
print("=" * 50)

def return_even_nums(numbers):
    number = []
    for num in numbers:
        if num % 2 == 0:
            number.append(num)
    return number

digit = return_even_nums([1, 4, 5, 7, 8, 6])
print(digit)
print("=" * 50)

a = [1, 2, 3,]
b = [4, 5, 6]
print(a + b)
print("=" * 50)

things =["lamb", "kit", "yam", "kings", "dogs", "man"]
new_things =[]
for word in things:
    if len(word) > 3:
        new_things.append(word)
print(new_things)
"""
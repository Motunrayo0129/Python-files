"""
days_per_month = {'jan': 31, 'feb': 28, 'mar': 31, 'apr': 30, 'may': 31}
#for month_name in days_per_month.keys():
print(days_per_month, end = " ")
print()

days_per_month['may'] = 30
print(days_per_month, end=" ")
    #print(days_per_month[month_name], end = " ")

    #for number_of_days in days_per_month.values():
        #print
"""
def convert_numbers_to_words(numbers):
    numbers_to_words = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',

    }
    return numbers_to_words.get(numbers, "invalid number")


number = int(input("Enter a number: "))
numbers_in_words = convert_numbers_to_words(number)
print(numbers_in_words)



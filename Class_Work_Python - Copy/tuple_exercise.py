def unpack_collection(collection):
    results = [0, 0, 0, 0]
    for index in range(4):
        results[index] = collection[index]
    return results


my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(unpack_collection(my_list))


#Unpacking Collections
def unpacking_collection(collection):
    first_number, second_number, third_number, *_ = collection
    return first_number, second_number, third_number, _


print(unpacking_collection(my_list))


#Slicing Collections
def slicing_collection(numbers):
    return numbers[:10:3]


print(slicing_collection([2, 3, 4, 5, 6, 7, 8, 9, 11, 12]))
print('=' * 33)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12]
def isOdd(number):
    return number % 2 == 1
print(isOdd(2))
"""
def numbers_of_words_that_appeared(words):
    dictionary = {}
    for word in words:
        dictionary[word] = words.count(word)
    return dictionary
"""

def numbers_of_words_that_appeared(words):
    dictionary = {}
    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    return dictionary


print(numbers_of_words_that_appeared("google"))

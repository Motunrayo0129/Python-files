def unique_values(values):
    return sorted(set(values))

numbers = unique_values([1, 6, 6, 2, 8, 6, 7, 8, 9])
print(numbers)

words = unique_values(['q', 'z', 'b', 'c', 't', 't', 'u', 'l', 'e'])
print(words)
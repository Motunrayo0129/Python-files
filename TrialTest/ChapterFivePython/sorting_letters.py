def sorting_letters(words):
    words.sort()
    return words
def descending_sort(words):
    words.sort(reverse=True)
    return words
def unique_sort(words):
    return sorted(set(words))



print(sorting_letters(['b', 'b', 'c', 'j', 'e', 'f', 'i', 'h']))
print(descending_sort(['b', 'b', 'c', 'j', 'e', 'f', 'i', 'h']))
print(unique_sort(['b', 'b', 'c', 'j', 'e', 'f', 'i', 'h']))
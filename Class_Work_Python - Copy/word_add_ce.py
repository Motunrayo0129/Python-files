
def add_ce_to_word(word = "", to_add = "ce"):
    if len(word) % 2 != 0:
        new_word = word + to_add
        return new_word
    else:
        center = len(word) // 2
        half_word = word[:center]
        half_word2 = word[center:]
        return half_word + to_add + half_word2

print(add_ce_to_word("helloo", "ce"))


def add_word_to_word(word = "", to_add = "ce"):
    count = 0
    for letter in word:
        count = count + 1
        if count % 2 != 0:
            new_word = word + to_add
            return new_word

        else:
            center = count // 2
            half_word1 = word[:center]
            half_word2 = word[center:]
            new_word = half_word1 + to_add + half_word2
            return new_word




print(add_word_to_word("joye", "ce"))


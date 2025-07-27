def tuple_sorted(words):
    words_sorted = []
    for word in words:
        words_sorted.append(word)
        if words == sorted(words):
            return True

        

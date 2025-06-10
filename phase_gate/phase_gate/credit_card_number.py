def validate_card(card_number):
    length = len(card_number)
    if length < 15 or length > 16:
        return "Invalid length"

    if card_number[0] == 4 and length == 16:
        return "Visa Card"
    elif card_number[0] == 5 and length == 16:
        return "MasterCard"
    elif card_number[0] == 6 and length == 16:
        return "Discover Card"
    elif card_number[0] == 3 and length == 13 and card_number[1] == 7:
        return "American Express Card"
    else:
        return "Unknown Card Type"

def apply_luhn_algorithm(card_number):
    sum_digits = 0
    digit_double = False

    for num in reversed(card_number):
        digit = num
        if digit_double:
            digit *= 2
            if digit > 9:
                digit -= 9
        sum_digits += digit
        digit_double = not digit_double

    return "Valid" if sum_digits % 10 == 0 else "Invalid"

sample_card = [4, 5, 3, 9, 1, 4, 8, 8, 0, 3, 4, 3, 6, 4, 6, 7]
print(validate_card(sample_card))
print(apply_luhn_algorithm(sample_card))
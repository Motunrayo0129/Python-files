def evaluate_password_strength(password):
    length = len(password)
    
    if length < 8:
        return "Very Weak"
    elif length == 8:
        return "Weak"
    elif 8 < length <= 16:
        return "Strong"
    else:
        return "Very Strong"

password = input("Enter your password: ")
strength = evaluate_password_strength(password)
print("Password Strength:", strength)
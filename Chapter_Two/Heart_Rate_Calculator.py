age = int(input("Enter your age: "))

max_heart_rate = 220 - age

target_low_rate = int(max_heart_rate * 0.50)
target_high_rate = int(max_heart_rate * 0.85)

print("Your maximum heart rate is ",max_heart_rate, "beats per minute")
print("Your target heart rate range is ", target_low_rate, "to", target_high_rate, "beats per minute")

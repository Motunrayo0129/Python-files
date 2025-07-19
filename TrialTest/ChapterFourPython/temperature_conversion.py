def fahrenheit_to_celsius(celsius):
    return celsius * 9 / 5 + 32

print(f"{'celsius':>10} | {'fahrenheit':>10}")
print("_" * 25)

for c in range(0, 101):
    fahrenheit = fahrenheit_to_celsius(c)
    print(f"{c:7} | {fahrenheit:10.1f}")
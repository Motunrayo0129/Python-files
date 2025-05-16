print("   Multiplication Table")
print("    ", end="")
for col in range(1, 10):
    print(f"{col:>3}", end="")
print("\n    " + "-" * 27)

for col in range(1, 10):
    print(f"{col:<2} |", end="")
    for row in range(1, 10):
        print(f"{col * row:>3}", end="") 
    print()
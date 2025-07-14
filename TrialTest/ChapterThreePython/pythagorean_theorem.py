for a in range(1, 21):
    for b in range(1, 21):
        for c in range(1, 21):
            if a * a + b * b == c:
                print(f'{a} {b} {c}')
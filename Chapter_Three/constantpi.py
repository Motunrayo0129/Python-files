target_values = ["3.14", "3.141", "3.1415", "3.14159"]
targets_reached = {}

pi_approx = 0
sign = 1
term_count = 0

print(f"{'Terms':>5} {'Approximation of π'}")

while len(targets_reached) < len(target_values):
    denominator = 2 * term_count + 1
    pi_approx += sign * (4 / denominator)
    term_count += 1
    sign *= -1  

    print(f"{term_count:>5} {pi_approx:.10f}")

    for target in target_values:
        if target not in targets_reached and f"{pi_approx:.10f}".startswith(target):
            targets_reached[target] = term_count

print("\nTerms needed to reach each accuracy level:")
for target, terms in targets_reached.items():
    print(f"{target} reached at term: {terms}")
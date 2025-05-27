import statistics

data = [9, 11, 22, 34, 17, 22, 34, 22, 40]

mean_value = statistics.mean(data)
median_value = statistics.median(data)
mode_value = statistics.mode(data)

print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
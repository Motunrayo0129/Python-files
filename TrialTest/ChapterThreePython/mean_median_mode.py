import statistics
values = [9, 11, 22, 34, 17, 22, 34, 22, 40]
mean = statistics.mean(values)
median = statistics.median(values)
mode = statistics.mode(values)
print(mean)
print(median)
print(mode)
print()


print('median without statistics')
value = [9, 11, 22, 34, 17, 22, 34, 22, 40]
value.sort()
index = len(value)

if index % 2 == 1:
    result = value [index // 2]
    print(result)
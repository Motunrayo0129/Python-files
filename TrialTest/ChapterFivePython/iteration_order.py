integers = [[1, 2, 3], [4, 5, 6]]
for index, row in enumerate(integers):
    for indices, column in enumerate(row):
        print(f"integers[{index}][{indices}]: {column}")
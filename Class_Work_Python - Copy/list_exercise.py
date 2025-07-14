scores = [[78, 45, 70, 59], [33, 80, 56, 47], [54,20,67]]
for index, score in enumerate(scores):
    for inner_index, inner_score in enumerate(scores):
        print(f'index {inner_index}')
        print(f'{inner_index}: {inner_score}')

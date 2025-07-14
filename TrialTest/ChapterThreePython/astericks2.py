rows = 10

for pat in range(1, rows + 1):
   print(f'*' * pat + ' ' * (rows - pat) + f'*' * (rows - pat + 1) + '' * (pat - 1) + f'  ' * (pat - 1) + '*' * (rows - pat + 1) + f' ' * (rows - pat) +  '*' * pat )
rows = int(input())
matrix = []
primary_diagonal = []
secondary_diagonal = []

for i in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

for row_index in range(rows):
    for col_index in range(rows):
        if row_index == col_index:
            primary_diagonal.append(matrix[row_index][col_index])
    secondary_diagonal.append(matrix[row_index][rows - 1 - row_index])

summary_prim = sum(primary_diagonal)
summary_sec = sum(secondary_diagonal)
print(f'Primary diagonal: {", ".join([str(p) for p in primary_diagonal])}. Sum: {summary_prim}')
print(f'Secondary diagonal: {", ".join([str(p) for p in secondary_diagonal])}. Sum: {summary_sec}')

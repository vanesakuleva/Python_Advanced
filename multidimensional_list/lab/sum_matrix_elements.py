rows, cols = [int(el) for el in input().split(', ')]
matrix = []
sums = 0
for i in range(rows):
    mat_rows = [int(el) for el in input().split(', ')]
    matrix.append(mat_rows)
    sums += sum(mat_rows)
print(sums)
print(matrix)

rows, cols = [int(i) for i in input().split()]
matrix = []
counter = 0
current_matrix = []

for n in range(rows):
    matrix.append(input().split())

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        if matrix[row_index][col_index] == matrix[row_index][col_index + 1] == matrix[row_index + 1][col_index] == matrix[row_index + 1][col_index + 1]:
            counter += 1
print(counter)

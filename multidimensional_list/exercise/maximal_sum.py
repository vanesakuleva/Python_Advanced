rows, cols = [int(i) for i in input().split()]
matrix = []
biggest = -999999999999999999
current_matrix = []
row_in= 0
col_in=0
summary = 0
final_sum = 0

for n in range(rows):
    matrix.append([int(l) for l in input().split()])

for row_index in range(rows - 2):
    for col_index in range(cols - 2):
        current_matrix = matrix[row_index][col_index] + matrix[row_index][col_index + 1]+ matrix[row_index][col_index + 2] + matrix[row_index + 1][col_index] + matrix[row_index + 1][col_index + 1] +matrix[row_index + 1][col_index + 2] + matrix[row_index + 2][col_index] + matrix[row_index + 2][col_index + 1] + matrix[row_index + 2][col_index + 2]
        if current_matrix > biggest:
            row_in = row_index
            col_in = col_index
            biggest = current_matrix


print(f'Sum = {biggest}')
print(matrix[row_in][col_in], matrix[row_in][col_in + 1],matrix[row_in][col_in + 2])
print(matrix[row_in + 1][col_in], matrix[row_in + 1][col_in + 1], matrix[row_in + 1][col_in + 2])
print(matrix[row_in + 2][col_in], matrix[row_in + 2][col_in+ 1], matrix[row_in + 2][col_in + 2])

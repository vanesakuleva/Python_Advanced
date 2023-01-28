rows, cols = [int(h) for h in input().split(', ')]
whole_matrix = []

for i in range(rows):
    matrix = [int(num) for num in input().split(' ')]
    whole_matrix.append(matrix)


for col_index in range(cols):
    summary = 0
    for row_index in range(rows):
        summary += whole_matrix[row_index][col_index]
    print(summary)
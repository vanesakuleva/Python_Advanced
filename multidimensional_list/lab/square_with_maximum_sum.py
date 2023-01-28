rows, cols = [int(x) for x in input().split(', ')]
matrix = []
max_sum = -999999999999999999
current_sub_matrix = []
final_matrix = []

for i in range(rows):
    nums = [int(y) for y in input().split(', ')]
    matrix.append(nums)

for row_index in range(rows-1):
    for col_index in range(cols-1):
        current_sub_matrix = [matrix[row_index][col_index], matrix[row_index][col_index+1],matrix[row_index+1][col_index], matrix[row_index+1][col_index+1]]

        sum_matrix = sum(current_sub_matrix)
        if sum_matrix > max_sum:
            max_sum = sum_matrix
            final_matrix = current_sub_matrix.copy()


print(final_matrix[0], final_matrix[1])
print(final_matrix[2], final_matrix[3])
print(max_sum)

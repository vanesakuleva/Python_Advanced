rows = int(input())
matrix = []

bunny = 'B'
directions = {"left": (0, -1), "right": (0, 1), "down": (1, 0), "up": (-1, 0)}
biggest_sum = 0
biggest_dir = 0
current_sum = 0
cur_num = 0
list_of_bigest_index = []
list_of_curr_index = []

for row in range(rows):
    matrix.append([x for x in input().split()])

columns = len(matrix[0])


def is_in_range(nxt_row, nxt_col, rows, cols):
    if 0 <= nxt_row < rows and 0 <= nxt_col < cols:
        return True
    return False


for row in range(rows):
    for col in range(columns):
        if matrix[row][col] == bunny:
            for direction in directions:
                next_row = row + directions[direction][0]
                next_col = col + directions[direction][1]
                while is_in_range(next_row, next_col, rows, columns):
                    if matrix[next_row][next_col].isdigit():
                        cur_num = int(matrix[next_row][next_col])
                        current_sum += cur_num
                        list_of_curr_index.append([next_row, next_col])
                    if matrix[next_row][next_col] == 'X':
                        break
                    next_row += directions[direction][0]
                    next_col += directions[direction][1]
                if current_sum >= biggest_sum:
                    biggest_sum = current_sum
                    biggest_dir = direction
                    list_of_bigest_index = list_of_curr_index
                    current_sum= 0
                    list_of_curr_index=[]

print(biggest_dir)
for i in list_of_bigest_index:
    print(i)
print(biggest_sum)

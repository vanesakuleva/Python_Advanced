rows = int(input())
command = [comm for comm in input().split()]
matrix = []
next_row = 0
next_col = 0
boolean = True
counter_of_collected = 0
index_of_collected = []
directions = {"left": (0, -1), "right": (0, 1), "down": (1, 0), "up": (-1, 0)}
current_row = 0
current_col = 0
counter = 0

for row in range(rows):
    matrix.append([x for x in input().split()])


def is_in_range(nxt_row, nxt_col, r):
    if 0 <= nxt_row < r and 0 <= nxt_col < r:
        return True
    return False




for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == 's':
            current_row = row
            current_col = col

for i in range(len(command)):
    direction = command[i]
    next_row = current_row + directions[direction][0]
    next_col = current_col + directions[direction][1]
    if is_in_range(next_row, next_col, rows):
        if matrix[next_row][next_col] == 'c':
            counter_of_collected += 1
            index_of_collected.append([next_row, next_col])
            matrix[next_row][next_col] = '*'
        if matrix[next_row][next_col] == 'e':
            print(f'Game over! {next_row, next_col}')
            boolean = False
            break
        current_row += directions[direction][0]
        current_col += directions[direction][1]

for i in range(rows):
    for j in range(rows):
        if matrix[i][j] == 'c':
            counter += 1

if counter == 0:
    print(f'You collected all coal! {current_row, current_col}')
if counter > 0 and boolean == True:
    print(f'{counter} pieces of coal left. {current_row, current_col}')

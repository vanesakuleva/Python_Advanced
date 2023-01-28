rows = 5
cols = 5
matrix = []
directions = {"left": (0, -1), "right": (0, 1), "down": (1, 0), "up": (-1, 0)}
command = ''
steps = 0
counter_of_x = 0
current_row = 0
current_col = 0
killed_x = 0
index_of_killed= []

for i in range(rows):
    matrix.append([i for i in input().split()])

for i in matrix:
    for j in i:
        if j == 'x':
            counter_of_x += 1


def is_in_range(nxt_row, nxt_col, r):
    if 0 <= nxt_row < r and 0 <= nxt_col < r:
        return True
    return False


for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == 'A':
            current_row = row
            current_col = col

count_of_comm = int(input())
for i in range(count_of_comm):
    commands = input().split()
    command = commands[0]
    direction = commands[1]
    next_row = current_row + directions[direction][0]
    next_col = current_col + directions[direction][1]
    if command == 'move':
        steps = int(commands[2])
        for i in range(steps):
            if is_in_range(next_row, next_col, rows):
                if matrix[next_row][next_col] == '.':
                    current_row += directions[direction][0]
                    current_col += directions[direction][1]
    if command == 'shoot':
        while is_in_range(next_row, next_col, rows) :
            if matrix[next_row][next_col] == 'x':
                killed_x += 1
                index_of_killed.append([next_row, next_col])
                matrix[next_row][next_col] = '.'
                break
            next_row += directions[direction][0]
            next_col += directions[direction][1]

if killed_x < counter_of_x:
    print(f'Training not completed! {counter_of_x-killed_x} targets left.')
    if index_of_killed:
        for i in index_of_killed:
            print(i)
elif killed_x == counter_of_x :
    print(f'Training completed! All {counter_of_x} targets hit.')
    for i in index_of_killed:
        print(i)


rows = int(input())
matrix = []
directions = {"left": (0, -1), "right": (0, 1), "down": (1, 0), "up": (-1, 0)}
current_row = 0
current_col = 0
counter_of_bags = 0
mtr = []
ten_bags = False
fail=False

for i in range(rows):
    mtr = input().split()
    matrix.append(mtr)

for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == 'A':
            current_row = row
            current_col = col

direction = input()
while direction:
    next_row = current_row + directions[direction][0]
    next_col = current_col + directions[direction][1]
    if matrix[next_row][next_col].isdigit():
        counter_of_bags += int(matrix[next_row][next_col])
        matrix[next_row][next_col] = '*'
        if counter_of_bags > 10:
            ten_bags = True
            break
    if matrix[next_row][next_col] == 'R':
        matrix[next_row][next_col] = '*'
        fail = True
        break

    matrix[next_row][next_col] = '*'
    current_row= next_row
    current_col=next_col

    direction = input()

print(matrix)

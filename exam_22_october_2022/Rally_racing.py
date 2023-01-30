rows = int(input())
racing_number = int(input())

current_row = 0
current_col = 0
km_passed = 0
matrix = []
boolean = True
directions = {"left": (0, -1), "right": (0, 1), "down": (1, 0), "up": (-1, 0)}

for row in range(rows):
    matrix.append([x for x in input().split()])


def is_in_range(nxt_row, nxt_col, r):
    if 0 <= nxt_row < r and 0 <= nxt_col < r:
        return True
    return False


direction = input()
matrix[current_row][current_col] = 'C'
while direction != 'End':
    next_row = current_row + directions[direction][0]
    next_col = current_col + directions[direction][1]

    if is_in_range(next_row, next_col, rows):
        if matrix[next_row][next_col] == '.':
            matrix[current_row][current_col] = '.'
            km_passed += 10
            current_row = next_row
            current_col = next_col
            matrix[current_row][current_col] = 'C'
        elif matrix[next_row][next_col] == 'T':
            matrix[current_row][current_col] = '.'
            matrix[next_row][next_col] = '.'
            for row in range(rows):
                for col in range(rows):
                    if matrix[row][col] == 'T':
                        current_row = row
                        current_col = col
                        matrix[current_row][current_col] = 'C'
                        km_passed += 30
        elif matrix[next_row][next_col] == 'F':
            matrix[current_row][current_col] = '.'
            current_row = next_row
            current_col = next_col
            km_passed += 10
            boolean = False
            matrix[next_row][next_col] = 'C'
            break
    direction = input()

if not boolean:
    print(f"Racing car {racing_number} finished the stage!")
    print(f"Distance covered {km_passed} km.")
else:
    print(f"Racing car {racing_number} DNF.")
    print(f"Distance covered {km_passed} km.")

for i in matrix:
    print(''.join(i))


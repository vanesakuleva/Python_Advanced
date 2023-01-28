rows = int(input())
matrix = []
coordinates_of_bombs = []

sum = 0
total_alive = 0
current_row = 0
current_col = 0
directions = {"left": (0, -1), "right": (0, 1), "down": (1, 0), "up": (-1, 0), "upright": (-1, 1),
              "upleft": (-1, -1), "downright": (1, 1), "downleft": (1, -1)}

for row in range(rows):
    matrix.append([int(x) for x in input().split()])

coordinates_of_bombs = [[u] for u in input().split()]


def is_in_range(nxt_row, nxt_col, r):
    if 0 <= nxt_row < r and 0 <= nxt_col < r:
        return True
    return False


for i in range(len(coordinates_of_bombs)):
    current = coordinates_of_bombs[0][0].split(',')
    current_row = int(current[0])
    current_col = int(current[1])
    coordinates_of_bombs.pop([0][0])
    value_of_bomb = matrix[current_row][current_col]
    if value_of_bomb > 0:
        matrix[current_row][current_col] = 0
        for direction in directions:
            next_row = current_row + directions[direction][0]
            next_col = current_col + directions[direction][1]
            if is_in_range(next_row, next_col, rows):
                if matrix[next_row][next_col] > 0:
                    matrix[next_row][next_col] -= value_of_bomb

for i in matrix:
    for j in i:
        if j > 0:
            total_alive += 1
            sum += j
print(f"Alive cells: {total_alive}")
print(f"Sum: {sum}")

for i in matrix:
    print(*i)

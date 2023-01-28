rows, cols = [int(h) for h in input().split(' ')]
matrix = []

for row_index in range(rows):
    matrix.append([x for x in input().split(' ')])


def is_outside(row, col, rows_m, cols_m):
    return row < 0 or col < 0 or row >= rows_m or col >= cols_m


command = input()

while command != 'END':
    shuffle_index = command.split(' ')
    if len(shuffle_index) == 5:
        row1, col1, rol2, col2 = [int(el) for el in shuffle_index[1:]]
    if len(shuffle_index) != 5 and shuffle_index[0] != 'swap':
        print('Invalid input!')

    elif is_outside(row1, col1, rows, cols) or is_outside(rol2, col2, rows, cols):
        print('Invalid input!')

    else:
        matrix[row1][col1], matrix[rol2][col2] = matrix[rol2][col2], matrix[row1][col1]

        for row in matrix:
            print(*row, sep=' ')
    command = input()
    
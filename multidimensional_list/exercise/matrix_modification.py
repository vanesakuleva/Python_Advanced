rows = int(input())
matrix = []
for row in range(rows):
    matrix.append([int(x) for x in input().split()])

coordinates = input()
while coordinates != 'END':
    coord = coordinates.split()
    if len(coord) == 4:
        command = coord[0]
        row = int(coord[1])
        col = int(coord[2])
        num = int(coord[3])
        if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
            if command == 'Add':
                matrix[row][col] += num
            elif command == 'Subtract':
                matrix[row][col] -= num
        else:
            print("Invalid coordinates")
    else:
        print("Invalid coordinates")
    coordinates = input()

for i in matrix:
    print(*i)

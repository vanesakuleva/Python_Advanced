rows, cols = [int(x) for x in input().split()]
word = input()
index = 0
matrix = []

for row in range(rows):
    matrix.append([])
    for col in range(cols):
        matrix[row].append(' ')

direction = 0
word_index = 0
col = 0
for row in range(rows):
    if row % 2 == 0:
        direction = 1
    else:
        direction = -1

    while 0 <= col < cols:
        matrix[row][col] = word[word_index]
        if word_index + 1 == len(word):
            word_index = -1
        word_index += 1
        col += direction
    col -= direction
    
for j in range(len(matrix)):
    print(''.join(matrix[j]))

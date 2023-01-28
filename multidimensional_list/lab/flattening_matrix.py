rows = int(input())
matrix = []


for i in range(rows):
    matrix_coll = [int(j) for j in input().split(', ')]
    matrix += matrix_coll
print(matrix)

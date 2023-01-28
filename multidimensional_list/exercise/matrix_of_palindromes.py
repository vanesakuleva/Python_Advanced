rows, cols = [int(h) for h in input().split(' ')]
matrix= []
nums= []

for row_index in range(rows):
    for col_index in range(cols):
        nums = [ chr(97+row_index),chr(97+ row_index + col_index),chr(97+row_index)]
        matrix.append(nums)

    print(* [''.join(x) for x in matrix])
    matrix = []






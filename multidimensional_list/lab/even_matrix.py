num_of_rows = int(input())
all=[]
for i in range(num_of_rows):
    matrix= [int(j) for j in input().split(', ') if int(j) %2==0]
    all.append(matrix)

print(all)


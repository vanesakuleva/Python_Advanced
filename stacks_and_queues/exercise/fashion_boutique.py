clothes= [int(x) for x in input().split(' ')]
capacity_of_rack= int(input())
counter_of_racks= 0
sum= 0

while clothes:
    top_cloth= clothes.pop()

    if sum + top_cloth  > capacity_of_rack:
        counter_of_racks+=1
        sum=0
    sum += top_cloth
if sum >0 :

    print(counter_of_racks+1)



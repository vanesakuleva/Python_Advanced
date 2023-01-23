from collections import deque
num_of_pumps = int(input())
pumps = deque()


for n in range(num_of_pumps):
    data= [int(x) for x in input().split()]
    pumps.append(data)

for i in range(num_of_pumps):
    tank = 0
    is_fail = False
    for fuel, distance in pumps:
        tank += fuel
        if distance>tank:
            is_fail = True
            break
        else:
            tank-= distance

    if is_fail:
        pumps.append(pumps.popleft())
    else:
        print(i)
        break

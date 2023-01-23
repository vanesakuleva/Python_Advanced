from collections import deque
total_food = int(input())
orders= deque([int(x) for x in input().split()])

print(max(orders))

while orders:
    finish_order= orders[0]
    if finish_order > total_food:
        break

    total_food -= finish_order
    orders.popleft()

if orders:
    print(f'Orders left: {" ".join([str(x) for x in orders])}')
else:
    print('Orders complete')
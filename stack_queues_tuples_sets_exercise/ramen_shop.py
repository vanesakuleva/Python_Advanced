from collections import deque

ramens = deque([int(x) for x in input().split(', ')])
clients = deque([int(x) for x in input().split(', ')])
customer = 0
ramen = 0


while ramens and clients:
    ramen = ramens.pop()
    customer = clients.popleft()
    if ramen > customer:
        ramen -= customer
        ramens.append(ramen)
    elif customer > ramen:
        customer -= ramen
        clients.appendleft(customer)

if len(ramens) < 1 and len(clients) > 1:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f'Customers left: {", ".join([str(x) for x in clients])}')
elif len(clients) < 1 and len(ramens) > 1:
    print('Great job! You served all the customers.')
    print(f'Bowls of ramen left: {", ".join([str(x) for x in ramens])}')
else:
    print('Great job! You served all the customers.')


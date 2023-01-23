from collections import deque

customer= input()
line= deque()


while customer!='End':
    if customer== 'Paid':
        while line:
            print(line.popleft())
    else:
        line.append(customer)
    customer= input()

print(f'{len(line)} people remaining.')
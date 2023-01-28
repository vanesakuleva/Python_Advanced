from collections import deque

bee = deque([int(x) for x in input().split(' ')])
nectar = [int(x) for x in input().split(' ')]
symbols = deque(input().split(' '))
total_honey = 0

while bee and nectar:
    present_bee = bee.popleft()
    present_nectar = nectar.pop()
    if present_nectar >= present_bee:
        symbol = symbols.popleft()
        if symbol == '+':
            total_honey += abs(present_bee + present_nectar)
        elif symbol == '-':
            total_honey += abs(present_bee - present_nectar)
        elif symbol == '*':
            total_honey += abs(present_bee * present_nectar)
        elif symbol == '/' and present_nectar > 0:
            total_honey += abs(present_bee / present_nectar)
    else:
        bee.appendleft(present_bee)

print(f'Total honey made: {total_honey}')
if bee:
    print(f'Bees left: {", ".join([str(x) for x in bee])}')
if nectar:
    print(f'Nectar left: {", ".join([str(x) for x in nectar])}')

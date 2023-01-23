from collections import deque
liters = int(input())
line= deque()
name = input()

while name != 'Start':
    line.append(name)

    name = input()

command = input()

while command != 'End':
    if command.isdigit():
        needed_liters = int(command)
        name = line.popleft()
        if liters >= needed_liters:
            liters -= needed_liters
            print(f'{name} got water')
        else:
            print(f'{name} must wait')

    else:
        lit_to_fill= int(command.split(' ')[1])
        liters+= lit_to_fill
    command = input()
print(f'{liters} liters left')

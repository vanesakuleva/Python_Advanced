from collections import deque

caffeine_milligrams = [int(i) for i in input().split(', ')]
energy_drinks = [int(i) for i in input().split(', ')]
energy_queue = deque(energy_drinks)
maximum_caffeine = 300
current_caffeine = 0
while energy_queue and caffeine_milligrams:
    drink = energy_queue.popleft()
    caffeine = caffeine_milligrams.pop()
    current_drink = drink * caffeine
    if current_caffeine + current_drink <= maximum_caffeine:
        current_caffeine += current_drink
    else:
        energy_queue.append(drink)
        if current_caffeine < 30:
            current_caffeine = 0
        else:
            current_caffeine -= 30

if len(energy_queue) == 0:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
else:
    print(f"Drinks left: {', '.join([str(x) for x in energy_queue])}")
print(f"Stamat is going to sleep with {current_caffeine} mg caffeine.")
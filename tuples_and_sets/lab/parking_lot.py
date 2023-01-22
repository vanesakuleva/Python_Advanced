num_of_cars = int(input())
cars=set()


for n in range(num_of_cars):
    command, number = input().split(', ')
    if command == 'IN':
      cars.add(number)
    elif command =='OUT' and number in cars:
        cars.remove(number)

if cars:
    for car in cars:
        print(car)
else:
    print(f"Parking Lot is Empty")
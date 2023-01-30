coffe_list = [ i for i in input().split()]
commands = int(input())

for i in range (commands):
    data  =input()
    command = data.split()[0]
    if command == 'Include':
        coffee  = data.split()[1]
        coffe_list.append(coffee)
    elif command  == 'Remove':
        first_last  = data.split()[1]
        cof_num = int(data.split()[2])
        if first_last=="first":
            for _ in range(cof_num):
                coffe_list.pop(0)
        elif first_last == "last":
            for _ in range (cof_num):
                coffe_list.pop()
    elif command == "Prefer":
        coffee_index_1 = int(data.split()[1])
        coffee_index_2 = int(data.split()[2])
        if coffee_index_1 in range(len(coffe_list)) and coffee_index_2 in range (len(coffe_list)):
            position1 = coffe_list[coffee_index_1]
            position2 = coffe_list[coffee_index_2]
            coffe_list[coffee_index_2]=position1
            coffe_list[coffee_index_1]=position2

    elif command == "Reverse":
        coffe_list.reverse()

print("Coffees:")
print(" ".join(coffe_list))

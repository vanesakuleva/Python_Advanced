number_of_opertion = int(input())

stack_of_num= []

for i in range(number_of_opertion):
    number = input()
    if number.split()[0] == '1':
        stack_of_num.append(int(number.split()[1]))
    elif number == '2' and stack_of_num:
        stack_of_num.pop()
    elif number == '3' and stack_of_num:
        print(max(stack_of_num))
    elif number =='4' and stack_of_num:
        print(min(stack_of_num))

while stack_of_num:
    el= stack_of_num.pop()
    if stack_of_num:
        print(el, end=', ')
    else:
        print(el)


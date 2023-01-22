number_of_names = int(input())
list_of_names= []

for n in range(number_of_names):
    names= input()
    list_of_names.append(names)

final_list= set(list_of_names)


for i in final_list:
    print(i)
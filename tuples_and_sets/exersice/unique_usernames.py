num = int(input())
set_of_names= set()

for n in range(num):
    name= input()
    set_of_names.add(name)

print('\n'.join(set_of_names))

num= int(input())

unique_el = set()

for i in range (num):
    elements= input().split(' ')
    for el in elements:
        unique_el.add(el)

for element in unique_el:
    print(element)
from collections import deque


box_of_materials= [int(x) for x in input().split(' ')]
magic_level = deque([int(x) for x in input().split(' ')])
doll_counter = 0
train_counter= 0
bear_counter= 0
bicycle_counter= 0
considered_task= False

while box_of_materials and magic_level:
    box= box_of_materials.pop()
    magic= magic_level.popleft()
    total_magic= box *magic
    if box !=0 and magic!=0:
        if total_magic<0:
            new= box+ magic
            box_of_materials.append(new)
        elif total_magic == 150:
            doll_counter+=1
        elif total_magic == 250:
            train_counter+=1
        elif total_magic == 300:
            bear_counter+=1
        elif total_magic == 400 :
            bicycle_counter+=1
        else:
            if total_magic >0 :
                box+=15
                box_of_materials.append(box)
    else:
        if box== 0:
            magic_level.appendleft(magic)
        elif magic== 0:
            box_of_materials.append(box)
if bicycle_counter >= 1 and bear_counter>=1 or doll_counter>=1 and train_counter>=1:
    considered_task= True

if considered_task:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if box_of_materials:
    print(f'Materials left: {", ".join([str(x) for x in reversed(box_of_materials)])}')
if magic_level:
    print(f'Magic left: {", ".join([str(x) for x in magic_level])}')

if bicycle_counter>0:
    print(f'Bicycle: {bicycle_counter}')
if doll_counter >0:
    print(f'Doll: {doll_counter}')
if bear_counter >0:
    print(f'Teddy bear: {bear_counter}')
if train_counter >0:
    print(f'Wooden train: {train_counter}')

# from collections import deque
#
# green_light = int(input())
# yellow_light = int(input())
# car_queue= deque()
# passed_cars= 0
# len_of_car=0
# time_for_other=0
# crash= False
#
#
# command= input()
#
# while command != 'END':
#     if command =='green':
#         while car_queue:
#             car = car_queue.popleft()
#             car_len = len(car)
#
#             green_time = green_light
#             if green_time >= car_len:
#                 green_time -= car_len
#                 passed_cars+=1
#
#
#             else:
#                 all_time = green_time + yellow_light
#                 if all_time > car_len:
#                     passed_cars+=1
#                     break
#                 else:
#                     index_of_crash = car_len - all_time
#                     crash=True
#                     print("A crash happened!")
#                     print(f"{car} was hit at {car[index_of_crash]}.")
#
#     else:
#         car_queue.append(command)
#     command = input()
# if not crash:
#     print("Everyone is safe.")
#     print(f"{passed_cars} total cars passed the crossroads.")






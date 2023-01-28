# from collections import deque
# chocolate=[int(x) for x in input().split(', ')]
# milk= deque([int(x) for x in input().split(', ')])
#
# milkshakes=0
# while chocolate and milk and milkshakes< 5:
#
#     current_choco=chocolate.pop()
#     current_milk=milk.popleft()
#     if current_choco> 0 and current_milk >0:
#         if current_choco == current_milk:
#             milkshakes += 1
#         else:
#             current_choco -= 5
#             chocolate.append(current_choco)
#             milk.appendleft(current_milk)
#     elif current_choco <= 0 :
#         milk.appendleft(current_milk)
#     elif current_milk <=0:
#         chocolate.append(current_choco)
#
#
# if milkshakes ==5:
#     print("Great! You made all the chocolate milkshakes needed!")
# else:
#     print("Not enough milkshakes.")
# if chocolate:
#     print(f"Chocolate: {', '.join([str(x) for x in chocolate])}")
# else:
#     print("Chocolate: empty")
# if milk:
#     print(f"Milk: {', '.join([str(x) for x in milk])}")
# else:
#     print("Milk: empty")


from collections import deque
chocolate=[int(x) for x in input().split(', ')]
milk= deque([int(x) for x in input().split(', ')])

milkshakes=0
while chocolate and milk and milkshakes< 5:

    current_choco=chocolate.pop()
    current_milk=milk.popleft()

    if current_choco <= 0 and current_milk <= 0 :
        continue

    if current_choco <=0:
        milk.appendleft(current_milk)
        continue
    if current_milk <= 0:
        chocolate.append(current_choco)
        continue

    if current_choco== current_milk:
        milkshakes+=1
    else:
        chocolate.append(current_choco-5)
        milk.append(current_milk)

if milkshakes ==5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolate:
    print(f"Chocolate: {', '.join([str(x) for x in chocolate])}")
else:
    print("Chocolate: empty")
if milk:
    print(f"Milk: {', '.join([str(x) for x in milk])}")
else:
    print("Milk: empty")

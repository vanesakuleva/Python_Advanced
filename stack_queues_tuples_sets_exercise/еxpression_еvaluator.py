from collections import deque

operation = input().split(' ')
num = deque()
result = 0

for element in operation:
    if element in '+-*/':
        while len(num) > 1:
            num_1 = num.popleft()
            num_2 = num.popleft()
            if element == "+":
                result = num_1 + num_2
            elif element == '-':
                result = num_1 - num_2
            elif element == '*':
                result = num_1 * num_2
            elif element == '/':
                result = num_1 // num_2

            num.appendleft(result)
    else:
        num.append(int(element))
print(num.popleft())

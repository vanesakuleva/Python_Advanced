text = input()
stack_for_parenthesis = []

for index in range(len(text)):
    if text[index] == '(':
        stack_for_parenthesis.append(index)
    elif text[index] ==')':
        start_index = stack_for_parenthesis.pop()
        print(text[start_index: index+1])


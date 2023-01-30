price_ratings = [int(i) for i in input().split(', ')]
entry_point = int(input())
items_type = input()
left = []
right = []
left_current_sum = 0
right_current_sum = 0
entry_value = price_ratings[entry_point]
for i in range(entry_point - 1, -1, -1):
    left.append(price_ratings[i])

for i in range(entry_point + 1, len(price_ratings), 1):
    right.append(price_ratings[i])

if items_type == 'cheap':

    for i in range(len(left)):
        current_number = left[i]
        if entry_value > current_number:
            left_current_sum += current_number

    for i in range(len(right)):
        current_number = right[i]

        if entry_value > current_number:
            right_current_sum += current_number

if items_type == 'expensive':
    for x in range(len(left)):
        current_number = left[x]
        if entry_value <= current_number:
            left_current_sum += current_number

    for x in range(len(right)):
        current_number = right[x]
        if entry_value <= current_number:
            right_current_sum += current_number


if left_current_sum>= right_current_sum:
    print(f'Left - {left_current_sum}')
else:
    print(f"Right - {right_current_sum}")
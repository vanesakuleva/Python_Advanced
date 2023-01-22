import math

rows = int(input())
sum_of_values = 0
even_set = set()
odd_set = set()
sum_of_even = 0
sum_of_odd = 0
for i in range(1, rows + 1):
    name = input()
    for letter in name:
        sum_of_values += ord(letter)
    sum_of_values = math.floor(sum_of_values / i)
    if sum_of_values % 2 == 0:
        even_set.add(sum_of_values)
        sum_of_even += sum_of_values
    else:
        odd_set.add(sum_of_values)
        sum_of_odd += sum_of_values
    sum_of_values = 0

if sum_of_odd == sum_of_even:
    result = (odd_set | even_set)
elif sum_of_odd > sum_of_even:
    result = (odd_set - even_set)
else:
    result = (odd_set ^ even_set)
print(*result, sep=', ')

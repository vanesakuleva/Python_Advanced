set_one = set([int(x) for x in input().split(' ')])
set_two = set([int(x) for x in input().split(' ')])
rows = int(input())



for i in range(rows):
    text = input().split(' ')
    command = text[0]
    witch_set = text[1]

    if command == 'Add':

        if witch_set == 'First':
            [set_one.add(int(x)) for x in text[2:]]
        elif witch_set == 'Second':
            [set_two.add(int(x)) for x in text[2:]]

    elif command == 'Remove':
        if witch_set == 'First':
            set_one=set_one.difference([int(x) for x in text[2:]])
        elif witch_set == 'Second':
            set_two = set_two.difference([int(x) for x in text[2:]])
    else:
        print(set_one.issubset(set_two) or set_two.issubset(set_one))

set_one=(sorted(set_one))
set_two= (sorted(set_two))
print(*set_one, sep=', ')
print(*set_two, sep= ', ')


summary = [int(x) for x in input().split()]


def what_is_the_sum(command, list_of_nums):
    if command == 'negative':
        num_list = [i for i in list_of_nums if i < 0]
    else:
        num_list = [i for i in list_of_nums if i > 0]

    return sum(num_list)


print(what_is_the_sum('negative', summary))

print(what_is_the_sum('positive', summary))

if abs(what_is_the_sum('negative', summary)) > what_is_the_sum('positive', summary):
    print('The negatives are stronger than the positives')
else:
    print('The positives are stronger than the negatives')
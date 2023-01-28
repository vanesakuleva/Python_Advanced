new = []
sub_lists = [x for x in input().split('|')]
for i in sub_lists:
    result = i.split()
    if result:
        new.append(result)
new.reverse()

for i in new:
    print(*i, end=" ")


# sub_lists = input().split('|')
#
# matrix = []
# while sub_lists:
#     sub_list = sub_lists.pop().split()
#     for el in sub_list:
#         matrix.append(el)
#
# print(*matrix, sep=' ')

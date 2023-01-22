def intersections(ranges):
    start, end= [int(x) for x in ranges.split(',')]
    return set(range(start, end+1))

rows = int(input())
longest_intersection = set()

for i in range(rows):
    range_one, range_two = input().split('-')
    first_set = intersections(range_one)
    second_set= intersections(range_two)
    final_intersection = first_set & second_set
    if len(final_intersection) > len(longest_intersection):
        longest_intersection = final_intersection
longest_intersection= list(longest_intersection)
print(f'Longest intersection is {longest_intersection} with length {len(longest_intersection)}')
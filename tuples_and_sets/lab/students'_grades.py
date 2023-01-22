

num_of_students= int(input())
n={}

for i in range(num_of_students):
    student, grade= input().split(' ')
    grades= float(grade)
    if student not in n:
        n[student]= [grades]
    else:
        n[student].append(grades)

for data in n.items():
    avarage_gr = sum(data[1])/ len(data[1])
    print(f"{data[0]} -> {' '.join([f'{el:.2f}' for el in data[1]])}" f" (avg: {avarage_gr:.2f})")
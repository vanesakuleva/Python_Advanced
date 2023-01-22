n,m = [int(h) for h in input().split(' ')]
n_set=set()
m_set=set()

for i in range(n):
    num= input()
    n_set.add(num)

for _ in range(m):
    number= input()
    m_set.add(number)


z= n_set.intersection(m_set)

for i in z:
    print(i)
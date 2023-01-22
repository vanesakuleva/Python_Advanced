numbers= (float(num) for num in input().split(' '))
occ={}


for k in numbers:
    if k not in occ:
        occ[k] = 0
    occ[k] += 1

for k,v in occ.items():
    print(f"{k} - {v} times")
num_of_guests = int(input())
reservation_codes=[]
dont_come=[]

for i in range (num_of_guests):
    guest= input()
    reservation_codes.append(guest)

g= input()
while g!= 'END':
    if g in reservation_codes:
        reservation_codes.remove(g)

    g= input()

print(len(reservation_codes))
sorted_code = sorted(reservation_codes)
print('\n'.join(sorted_code))

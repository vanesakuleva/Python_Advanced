biscuits_per_worker_day = int(input())
workers = int(input())
needed_biscuts = int(input())
days = 30
total_biscuts = 0
for day in range(1, days + 1):

    biscuts_today = workers * biscuits_per_worker_day
    if day % 3 == 0:
        biscuts_today *= 0.75
    total_biscuts += int(biscuts_today)
diff = abs(total_biscuts-needed_biscuts)
percentage = diff / needed_biscuts * 100
print(f"You have produced {int(total_biscuts)} biscuits for the past month.")
if total_biscuts > needed_biscuts:
    print(f"You produce {percentage:.2f} percent more biscuits.")
elif needed_biscuts>total_biscuts:
    print(f"You produce {percentage:.2f} percent less biscuits.")


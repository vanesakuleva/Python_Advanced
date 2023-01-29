def even_odd(*args):
    command = args[-1]
    if command == 'even':
        nums = [i for i in args[0:-1] if i % 2 == 0]
        return (nums)
    elif command == 'odd':
        nums = [i for i in args[0:-1] if i % 2 != 0]
        return (nums)


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

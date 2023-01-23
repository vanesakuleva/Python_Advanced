text= input()

left_bracket=[]
balance=True

for ch in text:
    if ch in '([{':
        left_bracket.append(ch)
    elif not left_bracket:
        balance=False
        break

    else:
        last_left_br = left_bracket.pop()
        if f'{last_left_br}{ch}' not in '()[]{}':
            balance=False
            break
        else:
            balance=True
if balance:
    print('YES')
else:
    print('NO')
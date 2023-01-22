text = input()
dict_of_ch = {}


for ch in text:
    if ch not in dict_of_ch:
        dict_of_ch[ch] = 1
    else:
        dict_of_ch[ch]+=1



for key in sorted(dict_of_ch):
    print(f'{key}: {dict_of_ch[key]} time/s')


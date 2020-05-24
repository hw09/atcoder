# 貪欲法(Greedyアルゴリズム)
s = input()
while len(s) != 0:
    if s[-5:] == 'dream' or s[-5:] == 'erase':
        s = s[:-5]
    elif s[-6:] == 'eraser':
        s = s[:-6]
    elif s[-7:] == 'dreamer':
        s = s[:-7]
    else:
        break
print('YES' if len(s) == 0 else 'NO')

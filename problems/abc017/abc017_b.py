s = input()

s = s.replace('ch', '')
s = s.replace('o', '')
s = s.replace('k', '')
s = s.replace('u', '')

if len(s) == 0:
    print('YES')
else:
    print('NO')
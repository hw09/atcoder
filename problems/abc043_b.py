s = list(input())
ans = []
for v in s:
    if v == '0':
        ans.append('0')
    elif v == '1':
        ans.append('1')
    elif v == 'B':
        if len(ans) != 0:
            ans.pop()
print(''.join(ans))
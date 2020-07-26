w = input()
n = 'aiueo'
ans = ''
for i in w:
    if i not in n:
        ans += i
print(ans)
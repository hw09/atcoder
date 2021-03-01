s = input()
t = input()
ans = 2000
for i in range(len(s)-len(t)+1):
    cmp = 0
    for j in range(len(t)):
        if s[i+j] != t[j]:
            cmp += 1
    if ans > cmp:
        ans = cmp
print(ans)

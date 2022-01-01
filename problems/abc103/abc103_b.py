S = input()
T = input()
t = list(S)
ans = 'No'
for i in range(len(S)):
    if ''.join(t) == T:
        ans = 'Yes'
        break
    else:
        tmp = t.pop()
        t.insert(0, tmp)
print(ans)
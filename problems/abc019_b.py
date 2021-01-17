s = input()

pos = 0
ans = ''
cnt = 0
for i in range(len(s)):
    if s[i] == s[pos]:
        cnt += 1
    else:
        ans += s[pos] + str(cnt)
        cnt = 1
        pos = i
else:
    ans += s[pos] + str(cnt)
print(ans)

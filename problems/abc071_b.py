import string
s = input()
ans = 'None'
for i in string.ascii_lowercase:
    if i not in s:
        ans = i
        break
print(ans)

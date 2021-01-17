o = input()
e = input()

length = len(o) if len(o) > len(e) else len(e)
ans = ''
for i in range(length):
    try:
        ans += o[i]
        ans += e[i]
    except IndexError:
        pass
print(ans)
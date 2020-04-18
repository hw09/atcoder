N = input()
x = N[:1]*3
if N > x:
    ans = str(int(N[:1])+1)*3
else:
    ans = x
print(ans)
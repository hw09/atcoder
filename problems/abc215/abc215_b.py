N = int(input())

for k in range(100):
    if 2**k <= N:
        ans = k
    else:
        break
print(ans)
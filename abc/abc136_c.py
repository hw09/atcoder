n = int(input())
h = [int(x) for x in input().split()]
a = h[0]
ans = 'Yes'
for i in range(1, n-1):
    a = max(h[i], a)
    b = h[i+1]
    if a - b >= 2:
        ans = 'No'
        break
print(ans)
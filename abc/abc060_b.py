a, b, c = map(int, input().split())
ans = 'NO'
for i in range(1, 10*10):
    if a * i % b == c:
        ans = 'YES'
        break
print(ans)
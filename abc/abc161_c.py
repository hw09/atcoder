n, k = map(int, input().split())

ans = n % k
while True:
    pre = ans
    ans = min(ans, abs(ans-k))
    if pre == ans:
        break   
print(ans)
a, b, c = map(int, input().split())

ans = 'NO'
if (a == 5 and b == 7 and c == 5) or (a == 5 and b == 5 and c == 7) or (a == 7 and b == 5 and c == 5):
    ans = 'YES'
print(ans)
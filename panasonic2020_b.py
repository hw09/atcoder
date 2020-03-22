h, w = map(int, input().split())
ans = 0
if h % 2 == 0:
    ans = h//2*w
else:
    if w % 2 == 0:
        ans = ((h//2+1)*(w//2))+((h//2)*(w//2))
    else:
        ans = ((h//2+1)*(w//2+1)) + ((h//2)*(w//2))
print(ans)
x = int(input())

ans = 0
for i in range(1, x+1):
    ans = (i * (i+1)) / 2
    if ans >= x:
        print(i)
        break

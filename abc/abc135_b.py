N = int(input())
p = [int(x) for x in input().split()]
n = [int(y) for y in range(1, N+1)]
ans = 'YES'
count = 0
for i in range(N):
    if p[i] == n[i]:
        pass
    else:
        if count <= 1:
            count +=1
        else:
            ans = 'NO'
print(ans)
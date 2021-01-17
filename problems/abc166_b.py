n, k = map(int, input().split())
ans = [int(x) for x in range(1, n+1)]
for i in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for j in a:
        if j in ans:
            ans.remove(j)
print(len(ans))
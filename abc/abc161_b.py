n, m = map(int, input().split())
a = [int(x) for x in input().split()]

ng = sum(a) / (4 * m)
a.sort(reverse=True)
ans = 'Yes'
for i in a[:m]:
    if i < ng:
        ans = 'No'
print(ans)

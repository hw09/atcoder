n, m = map(int, input().split())

a = [False]*n
b = [False]*n
for i in range(m):
    left, right = map(int, input().split())
    if left == 1:
        b[right-1] = True
    if right == n:
        a[left-1] = True

ans = 'IMPOSSIBLE'
for i in range(n):
    if a[i] == True and b[i] == True:
        ans = 'POSSIBLE'
print(ans)

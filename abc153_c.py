N, K = map(int, input().split())
H = list(map(int, input().split()))
H.sort()
for i in range(K):
    if len(H) > 0:
        H.pop()
    else:
        H.append(0)
print(sum(H))
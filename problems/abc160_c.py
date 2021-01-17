K, N = map(int, input().split())
a = [int(x) for x in input().split()]

dist = [0] * (N + 1)

for i in range(N-1):
    dist[i] = a[i+1] - a[i]

dist[N] = K - a[N - 1] + a[0]

print(K - max(dist))

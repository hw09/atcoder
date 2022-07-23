k, x = map(int, input().split())
ans = [int(x) for x in range(x-k+1, x+k)]
print(' '.join(map(str, ans)))
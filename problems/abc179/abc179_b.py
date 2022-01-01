N = int(input())

count = 0
maxCount = 0

for _ in range(N):
    a, b = map(int, input().split())
    if a == b:
        count += 1
        maxCount = max(count, maxCount)
    else:
        count = 0

print('Yes' if maxCount >= 3 else 'No')

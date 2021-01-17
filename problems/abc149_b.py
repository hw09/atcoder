A, B, K = map(int, input().split())

if(K >= A):
    result1 = 0
    x = K - A
    B = B - x
    result2 = B if B >= 0 else 0
else:
    result1 = A - K
    result2 = B

print('{} {}'.format(result1, result2))

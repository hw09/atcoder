n, m = map(int, input().split())
if n > 12:
    n -= 12
M = m * (360/60)
N = n * (360/12) + m * 0.5

angle = abs(N - M)
if angle > 180:
    angle = 360 - angle
print(angle)
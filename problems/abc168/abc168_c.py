import math
a, b, h, m = map(int, input().split())
H = 30 * h + 0.5 * m
M = 6 * m
angle = abs(H - M)
if angle >= 180:
    angle = 360 - angle
ans = a**2 + b**2 - (2 * a * b * math.cos(math.radians(angle)))
print(math.sqrt(ans))
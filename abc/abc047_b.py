w, h, n = map(int, input().split())
start = [0, 0]
end = [w, h]
for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        start[0] = max(start[0], x)
    elif a == 2:
        end[0] = min(end[0], x)
    elif a == 3:
        start[1] = max(start[1], y)
    elif a == 4:
        end[1] = min(end[1], y)

if end[0] - start[0] > 0 and end[1] - start[1] > 0:
    print((end[0] - start[0])*(end[1] - start[1]))
else:
    print(0)

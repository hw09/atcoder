A, B, C, D = map(int, input().split())

blue = A
red = 0

if blue <= red * D:
    print(0)
    exit()

for i in range(10**5):
    blue = blue + B
    red = red + C
    if blue <= red * D:
        print(i+1)
        exit()

print(-1)
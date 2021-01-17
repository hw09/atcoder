a = int(input())
b = int(input())

ab = a - (a//b * b)
print(b - ab if ab != 0 else 0)


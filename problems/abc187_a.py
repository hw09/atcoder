A, B = map(int, input().split())

a = 0
b = 0
for c in str(A):
    a += int(c)

for c in str(B):
    b += int(c)

if a >= b:
    print(a)
else:
    print(b)
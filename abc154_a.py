S, T = input().split()
A, B = input().split()
U = input()

if U == S:
    A = int(A) - 1
else:
    B = int(B) - 1
print('{} {}'.format(int(A), int(B)))

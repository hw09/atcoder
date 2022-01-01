a11, a12, a13 = map(int, input().split())
a21, a22, a23 = map(int, input().split())
a31, a32, a33 = map(int, input().split())
A = [a11, a12, a13, a21, a22, a23, a31, a32, a33]
N = int(input())
b = []
for _ in range(N):
    try:
        A[A.index(int(input()))] = '○'
    except ValueError:
        pass

ans = 'No'
if A[0] == '○' and A[1] == '○' and A[2] == '○':
    ans = 'Yes'
if A[3] == '○' and A[4] == '○' and A[5] == '○':
    ans = 'Yes'
if A[6] == '○' and A[7] == '○' and A[8] == '○':
    ans = 'Yes'

if A[0] == '○' and A[3] == '○' and A[6] == '○':
    ans = 'Yes'
if A[1] == '○' and A[4] == '○' and A[7] == '○':
    ans = 'Yes'
if A[2] == '○' and A[5] == '○' and A[8] == '○':
    ans = 'Yes'

if A[0] == '○' and A[4] == '○' and A[8] == '○':
    ans = 'Yes'
if A[2] == '○' and A[4] == '○' and A[6] == '○':
    ans = 'Yes'

print(ans)

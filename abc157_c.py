import sys
N, M = map(int, input().split())
S = []
C = []
for _ in range(M):
    s, c = map(int, input().split())
    S.append(s)
    C.append(c)

a1 = 0
a2 = 0
a3 = 0
b = []
for i in range(len(S)):

    if S[i] == 1:
        a1 = C[i]
    if S[i] == 2:
        a2 = C[i]
    if S[i] == 3:
    b.append(S[i])

if N == 1:
    print(a3)
elif N == 2:
    print(a2*10+a3)
else:
    print(a1*100+a2*10+a3)

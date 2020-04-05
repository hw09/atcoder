N = int(input())
S, T = input().split()

R = []
for i in range(N):
    R.append(S[i])
    R.append(T[i])

print(''.join(R))

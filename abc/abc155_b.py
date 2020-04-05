N = int(input())
A = list(map(int, input().split())) 
E = []
for i in range(N):
    if A[i] % 2 == 0:
        E.append(A[i])

K = True
for j in range(len(E)):
    if E[j] % 5 == 0 and E[j] % 3 == 0:
        pass
    elif E[j] % 5 == 0:
        pass
    elif E[j] % 3 == 0:
        pass
    else:
        K = False

print('APPROVED' if K == True else 'DENIED')

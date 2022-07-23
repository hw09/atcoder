N = int(input())
A = list(map(int, input().split()))

st = []
ma = 0

for i in range(N):
    ma = max(ma, A[i])
    st.append(ma-A[i])

print(sum(st))

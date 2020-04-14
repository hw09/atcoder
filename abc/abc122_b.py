S = list(input())

ans = 0
acgt = ['A', 'C', 'G', 'T']
conti = 0

for i in S:
    if i in acgt:
        conti += 1
        if ans < conti:
            ans = conti
    else:
        conti = 0

print(ans)

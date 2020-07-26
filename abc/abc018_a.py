abc = [int(input()) for _ in range(3)]

for i in abc:
    ans = 0
    for j in range(len(abc)):
        if abc[j] >= i:
            ans += 1
    print(ans)

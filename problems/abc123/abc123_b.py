X = [int(input()) for _ in range(5)]
ans = 0
ma = 10

for i in range(len(X)):
    ans += (-(-X[i]//10)) * 10
    if X[i]%10 != 0:
        if X[i]%10 < ma:
            ma = X[i]%10
print(ans - (10 - ma))
n, a, b = map(int, input().split())
ans = 0
for i in range(n):
    s, d = list(input().split())
    if s == 'East':
        if int(d) < a:
            ans += a
        elif int(d) > b:
            ans += b
        else:
            ans += int(d)
    elif s == 'West':
        if int(d) < a:
            ans -= a
        elif int(d) > b:
            ans -= b
        else:
            ans -= int(d)
if ans < 0:
    print('West ' + str(-ans))
elif ans > 0:
    print('East ' + str(ans))
else:
    print(0)
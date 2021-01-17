m = int(input())
ans = 89
if m < 100:
    ans = 0
elif m <= 5000:
    ans = m/1000 * 10
elif m <= 30000:
    ans = m/1000 + 50
elif m <= 70000:
    ans = (((m/1000 - 30) / 5) + 80)

if ans < 10:
    ans = '0' + str(int(ans))
else:
    ans = str(int(ans))

print(ans)
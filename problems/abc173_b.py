n = int(input())
s = [input() for _ in range(n)]

ans = [0]*4
for i in range(n):
    if s[i] == 'AC':
        ans[0] += 1
    elif s[i] == 'WA':
        ans[1] += 1
    elif s[i] == 'TLE':
        ans[2] += 1
    elif s[i] == 'RE':
        ans[3] += 1

print('AC x ' + str(ans[0]))
print('WA x ' + str(ans[1]))
print('TLE x ' + str(ans[2]))
print('RE x ' + str(ans[3]))

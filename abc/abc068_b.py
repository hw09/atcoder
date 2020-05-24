n = int(input())

def t(n):
    div = n
    cnt = 0
    while True:
        div, mod = divmod(div, 2)
        if mod == 0:
            cnt += 1
        else:
            return cnt

ans = 1
maxt = 0
for i in range(1, n+1):
    tt = t(i)
    if maxt < tt:
        maxt = tt
        ans = i
print(ans)  

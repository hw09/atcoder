N = int(input())

tops = ''
topt = 0
secs = ''
sect = 0

for _ in range(N):
    s, t = input().split()
    if topt < int(t):
        sect = topt
        secs = tops
        topt = int(t)
        tops = s
    elif sect < int(t):
        sect = int(t)
        secs = s

print(secs)

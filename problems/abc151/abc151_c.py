N, M = map(int, input().split())

ac_list = [0] * (N + 1)
wa_list = [0] * (N + 1)
a = 0
w = 0
for i in range(M):
    l = input().split()
    if ac_list[int(l[0])]!='AC':
        if l[1] == 'AC':
            ac_list[int(l[0])] = 'AC'
            a += 1
            w += wa_list[int(l[0])]
        else:
            wa_list[int(l[0])] += 1

print('{} {}'.format(a, w))

n = input()
nl = n[-1:]
hon = [2, 4, 5, 7, 9]
pon = [0, 1, 6, 8]
if int(nl) in hon:
    print('hon')
elif int(nl) in pon:
    print('pon')
else:
    print('bon')

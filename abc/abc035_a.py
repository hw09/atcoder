w, h = map(int, input().split())

if w / h > 1.5:
    print('16:9')
else:
    print('4:3')
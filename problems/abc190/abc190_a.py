A, B, C = map(int, input().split())

if A < B:
    print('Aoki')
elif A > B:
    print('Takahashi')
else:
    if C == 0:
        print('Aoki')
    else:
        print('Takahashi')

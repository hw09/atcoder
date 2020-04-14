S = input()

L = int(S[:2])
R = int(S[2:])

if 0 < L <= 12:
    if 0 < R <= 12:
        print('AMBIGUOUS')
    else:
        print('MMYY')
elif 0 < R <= 12:
    print('YYMM')
else:
    print('NA')

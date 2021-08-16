S = []
for _ in range(4):
    S.append(input())

print('Yes' if len(set(S)) == 4 else 'No')

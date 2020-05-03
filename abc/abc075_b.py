h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
ans = [[0]*w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            ans[i][j] = '#'
            if i > 0 and j > 0 and ans[i-1][j-1] != '#':
                ans[i-1][j-1] += 1
            if i > 0 and ans[i-1][j] != '#':
                ans[i-1][j] += 1
            if i > 0 and j < w-1 and ans[i-1][j+1] != '#':
                ans[i-1][j+1] += 1
            if j > 0 and ans[i][j-1] != '#':
                ans[i][j-1] += 1
            if j < w-1 and ans[i][j+1] != '#':
                ans[i][j+1] += 1
            if i < h-1 and j > 0 and ans[i+1][j-1] != '#':
                ans[i+1][j-1] += 1
            if i < h-1 and ans[i+1][j] != '#':
                ans[i+1][j] += 1
            if i < h-1 and j < w-1 and ans[i+1][j+1] != '#':
                ans[i+1][j+1] += 1

for k in range(h):
    for m in range(w):
        print(str(ans[k][m]), end='')
    print()

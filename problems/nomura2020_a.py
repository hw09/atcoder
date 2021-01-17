h1, m1, h2, m2, k = map(int, input().split())

h3, m3 = divmod(k, 60)

dh = h2 - h3
dm = m2 - m3
if dm < 0:
    dh -= 1
    dm = 60 + dm



ah = dh - h1
am = dm - m1
if am < 0:
    ah -= 1
    am = 60 + am

ans = ah * 60 + am
print(ans)
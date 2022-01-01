n = int(input())
l = []
for i in range(n):
    l.append(input())

l_set = set(l[0])
l_list = list(l_set)
l_sorted = sorted(l_list)
ans = ''

for ch in l_sorted:
    cnt = min(l[i].count(ch) for i in range(n))
    ans += ch * cnt

print(ans)

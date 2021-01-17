a, b = map(int, input().split())
t = [0]
for i in range(1, 1000):
    t.append(i*(i+1)//2)
print(t[b-a]-b)
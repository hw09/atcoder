a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())

x = [a, b, c, d]
y = [b, c, d, e]

def chk(x, y):
    return(abs(x - y))


result = 'Yay!'
for i in x:
    for j in y:
        if i != j:
            if chk(i, j) > k:
                result = ':('

print(result)
import string
alf = 'zabcdefghijklmnopqrstuvwxy'
x = int(input())

def x2a(x):
    s = ''
    while x != 0:
        div, mod = divmod(x, 26)
        s += alf[mod]
        if mod != 0:
            x = div
        else:
            x = div -1
    return s[::-1]
print(x2a(x))

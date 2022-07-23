import fractions
a, b, c, d = map(int, input().split())
a -= 1
B = b - (b//c + b//d)+b//(c*d//fractions.gcd(c, d))
A = a - (a//c + a//d)+a//(c*d//fractions.gcd(c, d))

print(B - A)

Sx, Sy, Gx, Gy = map(int, input().split())
print(round(((-Sy*(Sx-Gx))+(Sx*(Sy+Gy)))/(Sy+Gy), 10))

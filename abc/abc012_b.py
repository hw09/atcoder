n = int(input())
ss = n % 60
mm = (n // 60) % 60
hh = n // 3600

print(f'{str(hh).zfill(2)}:{str(mm).zfill(2)}:{str(ss).zfill(2)}')
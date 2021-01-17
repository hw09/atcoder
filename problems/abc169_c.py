# pythonでは、小数型は通常２進法表示53bit分の有効数字しか持たず、それより下の位は切り捨てられてしまう。


import decimal
a, b = map(decimal.Decimal, input().split())
print(a * b // 1)
import datetime

S = input()
sdt = datetime.datetime.strptime(S, '%Y/%m/%d')
hdt = datetime.datetime.strptime('2019/04/30', '%Y/%m/%d')

print('TBD' if sdt > hdt else 'Heisei')

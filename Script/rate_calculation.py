import calendar
import time
print(time.localtime(time.time()).tm_year)
print('请输入金额：')
rate = 0.000795
Amount =int(input())
total = 7500
month_list= [6,7,8,9,10,11,12]
for month in month_list:
    total += calendar.monthrange(time.localtime(time.time()).tm_year,month)[-1]*float(rate)*Amount
    if month == 6 or month == 7:
        Amount = Amount
    else:
        Amount -= 1250
print(total)

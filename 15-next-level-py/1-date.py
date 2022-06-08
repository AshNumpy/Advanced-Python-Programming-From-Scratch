from datetime import datetime

res = datetime.today()
result = res.year

result = datetime.ctime(res)
result = datetime.strftime(res, '%Y %B %A')

t = '15 April 2022 hour 12:12:30'
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')

birthday = datetime(2000,9,15,3,30,0)

print(birthday)


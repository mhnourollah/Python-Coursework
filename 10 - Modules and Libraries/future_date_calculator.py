import datetime

today = datetime.date.today()

days = int(input())

future_date = today + datetime.timedelta(days=days)

print(future_date)

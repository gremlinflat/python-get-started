from  datetime import datetime, timedelta

current_date = datetime.now()

tanggal = input("Please input your first date : ")
first_date = datetime.strptime(tanggal, "%d/%m/%Y" ) 
yesterday = timedelta(days=1)

print(f"your first date is on {first_date}")
print(f"the day before it was {first_date-yesterday}")
print(f"day {first_date.day}")
print(f"month {first_date.month}")
print(f"year {first_date.year}")

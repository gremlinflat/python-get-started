from  datetime import datetime, timedelta

current_date = datetime.now()

tanggal = input("Please input your first date : ")
first_date = datetime.strptime(tanggal, "%d/%m/%Y" ) 

print(f"your first date is on {first_date}")
print(f"day {first_date.day}")
print(f"month {first_date.month}")
print(f"year {first_date.year}")

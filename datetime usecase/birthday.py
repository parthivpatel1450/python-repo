from datetime import datetime
from dateutil.relativedelta import relativedelta


year=int(input("Enter birth year: "))
month=int(input("Enter birth month: "))
day=int(input("Enetr birth day: "))

birthday=datetime(year,month,day)

today=datetime.now()

age=relativedelta(today,birthday)

print(f"\nYour age is {age.years} years and {age.months} months and {age.days} days")

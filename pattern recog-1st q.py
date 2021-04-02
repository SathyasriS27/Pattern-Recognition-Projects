import calendar 
from decimal import Decimal

def findDay(date,month,year): 
    day=date
    month=month 
    year=year   
    dayNumber = calendar.weekday(year, month, day) 
    days =["Monday", "Tuesday", "Wednesday", "Thursday", 
                         "Friday", "Saturday", "Sunday"] 
    return (days[dayNumber]) 
  
date=Decimal(input("enter the date in dd format"))
month=Decimal(input("enter the month is mm format"))
year=Decimal(input("enter the year in yyyy format"))

print("the day of the week is ")
print(findDay(date,month,year))

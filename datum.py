from datetime import date

day,month= list(map(int,input().split()))
givenDate = date(2009, month, day)
weekday = givenDate.strftime("%A")
print(weekday)
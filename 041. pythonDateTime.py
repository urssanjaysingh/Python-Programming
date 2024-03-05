# current date
import datetime as dt 
current_date = dt.date.today()
print(current_date)

# date class
import datetime as dt 
date1 = dt.date(2021, 1, 5)
print(date1)
print("Year:", date1.year)
print("Month:", date1.month)
print("Day:", date1.day)

# time class
import datetime as dt 
time1 = dt.time(10, 45, 30, 45667)
print(time1)
print("Hour:", time1.hour)
print("Minute:", time1.minute)
print("Second:", time1.second)
print("Microseconds:", time1.microsecond)

# date with time
import datetime as dt
datetime_obj = dt.datetime(2021, 11, 28, 23, 55, 59)
print(datetime_obj)
print(datetime_obj.date())
print(datetime_obj.time())

# getting current date and time
import datetime as dt
current_datetime = dt.datetime.now()
print(current_datetime)

# remaining days and time
import datetime as dt 
current_time = dt.datetime.now()
next_new_year = dt.datetime(2022, 1, 1)
time_remaining = next_new_year - current_time
print(time_remaining)

# strftime() method formats datetime
import datetime as dt
current_datetime = dt.datetime.now()
print(current_datetime)
string_date = current_datetime.strftime("%A, %B, %d, %Y")
print(string_date)

# strptime() method converts strings to datetime objects.
import datetime as dt
date_string = "21 June, 2021"
date_object = dt.datetime.strptime(date_string, "%d %B, %Y")
print("Date object:", date_object)
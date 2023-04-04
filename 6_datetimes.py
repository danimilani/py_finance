# Datetimes and Dictionaries

# Datetime Module and Objects

# The objects have attributes representing year, month, date, hour, second, microsecond and timezone
# To create datetime object you need to provide at lease year, month and date

from datetime import datetime
blackmonday = datetime(1987,10,19)
print(black_monday)

# Datetime Now - shows current time

datetime.now()

# Datetime from String - using string parse time function

black_monday_str = "Monday, October 19, 1987. 9:30 am" #string to convert
format_str = "%A, %B, %d, %Y. %I:%M %p" #format string
datetime.datetime.strptime(black_monday_str, format_str)

"""
Year

%y - without century
%Y - with century

Month

%b - Abbreviated Names (jan, feb..)
%B - Full names (January, February...)
%m - As numbers (01,02...12)

Day of Month

%d (01,02...31)

Weekday

%a - Abbreviated Name (Sun, Sat)
%A - full name (sunday, saturday)
%w - number (0...6)

Hour

%H - 24 hour (00...23)
%I - 12 hour (01...12)
%M - minutes as number (01...59)

Seconds

%S (00...59)

Micro-Seconds

%f (000000....999999)

AM/PM

%p (AM, PM)
"""

# String from datetime

dt.strftime(format_string)

great_depression_crash = datetime.datetime(1929, 10, 29)
great_depression_crash

great_depression_crash.strftime("%a, %b, %d, %Y")
# Result: 'Tue, Oct 29, 1929'

##################################################

# EXERCISES

# Creating datetimes for dates

import datetime

# Date and time now
now = datetime.datetime.now()
print(now)

# Flash crash May 28, 1962
flash_crash = datetime.datetime(1962, 5, 28)
print(flash_crash)

# Black Monday Oct 19, 1987
black_monday = datetime.datetime(1987, 10, 19)
print(black_monday)

"""
2023-04-04 21:04:08.666371
1962-05-28 00:00:00
1987-10-19 00:00:00
"""

# Datetimes from strings

crash_text = "Friday the 13th, Oct, 1989"

# Create a format string mapping the text
crash_format_str = "%A the %dth, %b, %Y"
min_crash = datetime.datetime.strptime(crash_text, crash_format_str)
print(min_crash)

recession_text = "07/03/90"

# Create format string
recession_format_str = "%m/%d/%y"

# Create datetime from text using format string
nineties_rec = datetime.datetime.strptime(recession_text, recession_format_str)
print(nineties_rec)

"""
1989-10-13 00:00:00
1990-07-03 00:00:00
"""

# Converting format with datetimes

org_text = "Sep 16 1992"

# Format string for original text
org_format = "%b %d %Y"

# Create datetime for Black Wednesday - create datetime from a string
black_wednesday = datetime.datetime.strptime(org_text, org_format)
print(black_wednesday)

# New format: 'Wednesday, September 16, 1992'
new_format = "%A, %B %d, %Y"

# String in new format - create a string from a datetime
new_text = black_wednesday.strftime(new_format)
print(new_text)

"""
<script.py> output:
    1992-09-16 00:00:00
    Wednesday, September 16, 1992
"""








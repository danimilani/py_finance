# Datetimes and Dictionaries

# DATETIME #

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
# Comparing datetimes

from datetime import datetime
asian_crisis = datetime(1997,7,2)
world_mini_crash = datetime(1997,10,27)

asian_crisis > world_mini_crash
# Result : False

asian_crisis < world_mini_crash
# Result : True

text = "10/27/1997"
format_str = "%m/%d/%Y"
sell_date = datetime.strptime(text, format_str)

sell_date == world_mini_crash
# Result: true

# Time Delta

delta = world_mini_crash - asian_crisis

type(delta)
# Result: datetime.timedelta

delta.days
# Result: 117

# Creating Relative Datetimes
# Create your own timedelta and use it as an offset to create a relative datetime

from datetime import timedelta
offset = timedelta(weeks = 1)
offset
# result: datetime.timedelta(7)

dt - offset
# result: datetime.datetime(2019,1,7,0,0)

offset = timedelta(days = 16)
dt - offset
# result: datetime.datetime(2019,12,29,0,0)

cur_week = last_week + timedelta(weeks = 1)
# Do some work with date
# set last week variable to cur week and repeat
last_week = cur_week

source_dt = event_dt - timedelta(weeks=4)
# Use source datetime to look up market factors

########################################################

# EXERCISES #

## Accessing datetime attributes

# March 10, 2000 Tech Bubble Crash
tech_bubble = datetime(2000, 3, 10)

# Access the year
yr  = tech_bubble.year

# Access the month
mth = tech_bubble.month

# Access the day
day = tech_bubble.day

print(f"Year: {yr}, Month: {mth}, Day: {day}")

<script.py> output:
    Year: 2000, Month: 3, Day: 10

## Comparing datetimes

# Lehman Brothers before Morgan Stanley?
lehman_first = lehman < morgan_stanley
print(f"It is {lehman_first} that Lehman Brothers declared bankruptcy first.") 
<script.py> output:
    It is True that Lehman Brothers declared bankruptcy first.

# Goldman Sachs after TARP?
tarp_first = goldman_sachs > tarp
print(f"It is {tarp_first} that TARP was approved first.")
<script.py> output:
    It is False that TARP was approved first.

# Goldman Sachs and Morgan Stanley same day?
same_time = goldman_sachs == morgan_stanley
print(f"It is {same_time} that Morgan Stanley and Goldman Sachs acted simultaneously")
<script.py> output:
    It is True that Morgan Stanley and Goldman Sachs acted simultaneously

## Making relative datetimes

# Create a datetime for one week before TARP was passed
from datetime import datetime, timedelta

# TARP passed Oct 3 2008
tarp = datetime(2008, 10, 3)

# Seven days before TARP
week_before = tarp - timedelta(days = 7)

# Print week_before
print(week_before)
<script.py> output:
    2008-09-26 00:00:00

# Create a datetime for one week after TARP was passed
from datetime import datetime, timedelta

# TARP passed Oct 3 2008
tarp = datetime(2008, 10, 3)

# One week after TARP
week_after = tarp + timedelta(weeks = 1)

# Print week_after
print(week_after)
<script.py> output:
    2008-10-10 00:00:00

# Create a datetime for one year after TARP was passed
from datetime import datetime, timedelta

# TARP passed Oct 3 2008
tarp = datetime(2008, 10, 3)

# One year after TARP
year_after = tarp + timedelta(weeks = 52)

# Print year_after
print(year_after)
<script.py> output:
    2009-10-02 00:00:00

########################################################

# DICTIONARIES #








# Manipulating Date and Time Series

# How to use dates & times with pandas

## Basic building block - pd.Timestamp

import pandas as pd
from datetime import datetime
time_stamp = pd.Timestamp(datetime(2017,1,1))
pd.Timestamp('2017-01-01') == time_stamp
time_stamp

# returns: Timestamp('2017-01-01 00:00:00') - Automatically sets the time to midnight

time_stamp.year #to retrieve the year
time_stamp.day_name() #to retrieve the weekday


## Time Period - pd.Period & freq

period = pd.Period('2017-01')
period #default : month-end
#returns: Period('2017-01', 'M')

period.asfreq('D') #convert to daily
#returns: Period('2017-01-31', 'D')

# To get Monthly Periods
period + 2
#returns: Period('2017-03', 'M')

## Time Period - Sequnces of dates & times

index = pd.date_range(start = '2017-1-1', periods=12, freq = 'M')
#the function returns the sequence of dates as a DateTimeIndex with frequency info.

# 1. EXERCISE - Your first time series

# Create the range of dates here
seven_days = pd.date_range(start = '2017-1-1', periods=7, freq = 'D')

# Iterate over the dates and print the number and name of the weekday
for day in seven_days:
    print(day.dayofweek, day.day_name())

"""
Results:
6 Sunday
0 Monday
1 Tuesday
2 Wednesday
3 Thursday
4 Friday
5 Saturday
"""

## Indexing & resampling time series

# Time series transformation

# Converting string dates to datetime64
google.date = pd.to_datetime(google.date)
google.info()

google.set_index('date', inplace=True) #inplace - dont create copy
google.info()

# Plotting the time series
google.price.plot(title='Google Stock Price')
plt.tight_layout(); plt.show()

# Partial String Indexing
# If you pass a string representing a year, pandas returns all the dates within this year
google['2015'].info() # Pass string for part of date
google['2015-3' : '2016-2'].info() # Slice includes last month
google.loc['2016-6-1', 'price'] # Use full date with .loc[]

# Set Frequency
google.asfreq('D').info() #set calendar day frequency
# Upsampling: the new DataFrame is of higher frequency as the original version (missing data)

google = google.asfreq('B') #change to calendar day frequency
google.info()

google[google.price.isnull()] #Select missing 'price' values


# EXERCISE 1 - Create a time series of air quality data

data = pd.read_csv('nyc.csv')

# Inspect data
print(data.info())

# Convert the date column to datetime64
data.date = pd.to_datetime(data.date)

# Set date column as index
data.set_index('date', inplace=True)

# Inspect data 
print(data.info())

# Plot data
data.plot(subplots=True)
plt.show()

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 6317 entries, 0 to 6316
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   date    6317 non-null   object 
 1   ozone   6317 non-null   float64
 2   pm25    6317 non-null   float64
 3   co      6317 non-null   float64
dtypes: float64(3), object(1)
memory usage: 197.5+ KB
None
<class 'pandas.core.frame.DataFrame'>
DatetimeIndex: 6317 entries, 1999-07-01 to 2017-03-31
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   ozone   6317 non-null   float64
 1   pm25    6317 non-null   float64
 2   co      6317 non-null   float64
dtypes: float64(3)
memory usage: 197.4 KB
None
"""

# EXERCISE 2 - Compare annual stock price trends

# Create dataframe prices here
prices = pd.DataFrame()

# Select data for each year and concatenate with prices here 
for year in ['2013', '2014', '2015']:
    price_per_year = yahoo.loc[year, ['price']].reset_index(drop=True)
    price_per_year.rename(columns={'price': year}, inplace=True)
    prices = pd.concat([prices, price_per_year], axis=1)

# Plot prices
prices.plot()
plt.show()

# EXERCISE 3  - Set and change time series frequency

# Inspect data
print(co.info())

# Set the frequency to calendar daily
co = co.asfreq('D')

# Plot the data
co.plot(subplots=True)
plt.show()

# Set frequency to monthly
co = co.asfreq('M')

# Plot the data
co.plot(subplots=True)
plt.show()

"""
<class 'pandas.core.frame.DataFrame'>
DatetimeIndex: 1898 entries, 2005-01-01 to 2010-12-31
Data columns (total 3 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   Chicago      1898 non-null   float64
 1   Los Angeles  1898 non-null   float64
 2   New York     1898 non-null   float64
dtypes: float64(3)
memory usage: 59.3 KB
None
"""

## Lags, changes, and returns for stock price series

google = pd.read_csv('google.csv', parse_dates=['date'], index_col='date')
google.info()
google.head()

# Method .shift() to move data between past and future

google['shifted'] = google.price.shift() # default: periods = 1
google['lagged'] = google.price.shift(periods=-1) #  move to the past

# Calculate one-period percent change 

google['return'] = google.change.sub(1).mul(100)

# Difference in value for two adjacent periods

google['diff'] = google.price.diff()

# Percentage change for two adjacent periods

google['diff'] = google.price.pct_change().mul(100)
google['diff'] = google.price.pct_change(periods = 3).mul(100)

# EXERCISE 1

# Import data here
google = pd.read_csv('google.csv', parse_dates=['Date'], index_col='Date')

# Set data frequency to business daily
google = google.asfreq('B')

# Create 'lagged' and 'shifted'
google['lagged'] = google.Close.shift(periods=-90)
google['shifted'] = google.Close.shift(periods=90)

# Plot the google price series
google.plot(subplots=True)
plt.show()

# EXERCISE 2 - Calculating stock price changes

# Created shifted_30 here
yahoo['shifted_30'] = yahoo.price.shift(30)

# Subtract shifted_30 from price
yahoo['change_30'] = yahoo.price.sub(yahoo.shifted_30)

# Get the 30-day price difference
yahoo['diff_30'] = yahoo.price.diff(30)

# Inspect the last five rows of price
print(yahoo.tail())

# Show the value_counts of the difference between change_30 and diff_30
print(yahoo.change_30.sub(yahoo.diff_30).value_counts())

"""
           price  shifted_30  change_30  diff_30
date                                             
2015-12-25    NaN       32.19        NaN      NaN
2015-12-28  33.60       32.94       0.66     0.66
2015-12-29  34.04       32.86       1.18     1.18
2015-12-30  33.37       32.98       0.39     0.39
2015-12-31  33.26       32.62       0.64     0.64
0.0    703
dtype: int64
"""

# EXERCISE 3 - Plotting multi-period returns

# Create daily_return
google['daily_return'] = google.Close.pct_change(periods = 1).mul(100)

# Create monthly_return
google['monthly_return'] = google.Close.pct_change(periods = 30).mul(100)

# Create annual_return
google['annual_return'] = google.Close.pct_change(periods = 360).mul(100)

# Plot the result
google.plot(subplots=True)
plt.show()




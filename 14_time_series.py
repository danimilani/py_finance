# CHAPTER 1 - Manipulating Date and Time Series

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

# CHAPTER 2 - Compare time series growth rates

# Comparing stock performance

# Normalizing a single series

google = pd.read_csv('google.csv', parse_dates=['date'], index_col = 'date')
google.head(3)
"""
date          price
2010-01-04    313.06
2010-01-05    311.68
2010-01-06    303.83
"""
first_price = google.price.iloc[0] #int-based selection
first_price
#result: 313.06

first_price == google.loc['2010-01-04','price']
#result: True

#divide the price series by its first price using div and multiplying by 100
normalized = google.price.div(first_price).mul(100)
normalized.plot(title='Google Normalized Series')

# Comparing with a benchmark - compare the performance of the stocks agains the broader stock market

index = pd.read_csv('benchmark.csv', parse_dates=['date'], index_col = 'date')
index.info()

prices = pd.concat([prices, index], axis = 1).dropna()
prices.info()

normalized = prices.div(prices.iloc[0]).mul(100)
normalized.plot()

# To show the performance difference for each stock relative to the benchmark in percentage points you
# can subtract the normalized SP500 from the normalized stock prices

diff = normalized[tickers].sub(normalized['SP500'], axis=0)
diff.plot()

# EXERCISE

# 1. Compare the performance of several asset classes
# To broaden your perspective on financial markets, let's compare four key assets: stocks, bonds, gold, and oil.

"""
              SP500   Bonds     Gold    Oil
DATE                                       
2007-06-29  1503.35  402.15   648.50  70.47
2007-07-02  1519.43  402.96   650.50  71.11
2007-07-03  1524.87  402.02   657.25  71.41
2007-07-05  1525.40  400.15   655.90  71.81
2007-07-06  1530.44  399.31   647.75  72.80
...             ...     ...      ...    ...
2017-06-20  2437.03  621.84  1246.50  43.34
2017-06-21  2435.61  622.94  1247.05  42.48
2017-06-22  2434.50  622.93  1251.40  42.53
2017-06-23  2438.30  623.57  1256.30  42.86
2017-06-26  2439.07  625.00  1240.85  43.24
"""

# Import data here
prices = pd.read_csv('asset_classes.csv', parse_dates=['DATE'], index_col='DATE')
# Inspect prices here
print(prices.info())
# Select first prices
first_prices = prices.iloc[0]
# Create normalized_prices
normalized = prices.div(first_prices).mul(100)
# Plot normalized_prices
normalized.plot()
plt.show()

"""
<class 'pandas.core.frame.DataFrame'>
DatetimeIndex: 2469 entries, 2007-06-29 to 2017-06-26
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   SP500   2469 non-null   float64
 1   Bonds   2469 non-null   float64
 2   Gold    2469 non-null   float64
 3   Oil     2469 non-null   float64
"""

# 2. Comparing stock prices with a benchmark

# Import stock prices and index here
stocks = pd.read_csv('nyse.csv', parse_dates=['date'], index_col='date')
dow_jones = pd.read_csv('dow_jones.csv', parse_dates=['date'], index_col='date')
# Concatenate data and inspect result here
data = pd.concat([stocks, dow_jones], axis=1)
print(data.info())

"""
DatetimeIndex: 1762 entries, 2010-01-04 to 2016-12-30
    Data columns (total 4 columns):
     #   Column  Non-Null Count  Dtype  
    ---  ------  --------------  -----  
     0   JNJ     1762 non-null   float64
     1   JPM     1762 non-null   float64
     2   XOM     1762 non-null   float64
     3   DJIA    1762 non-null   float64
"""
# Normalize and plot your data here
data.div(data.iloc[0]).mul(100).plot()
plt.show()

# 3. Plot performance difference vs benchmark index
# Let's compare the performance of Microsoft (MSFT) and Apple (AAPL) to the S&P 500 over the last 10 years.

# Create tickers
tickers = ['MSFT', 'AAPL']
# Import stock data here
stocks = pd.read_csv('msft_aapl.csv', parse_dates=['date'], index_col = 'date')
# Import index here
sp500 = pd.read_csv('sp500.csv', parse_dates=['date'], index_col = 'date')
# Concatenate stocks and index here
data = pd.concat([stocks,sp500], axis=1).dropna()
# Normalize data
normalized = data.div(data.iloc[0]).mul(100)
# Subtract the normalized index from the normalized stock prices, and plot the result
diff = normalized[tickers].sub(normalized['SP500'], axis=0)
diff.plot()
plt.show()

##############

# Changing the time series frequency: resampling

# Upsampling - fill or interpolate missing data - increasing the frequency of time-series
# Downsampling - aggregate existing data - decreasing the frequency of time-series

# UPSAMPLE - Quarterly Data to Monthly

dates = pd.date_range(start='2016', periods=4, freq='Q')
data = range(1,5)
quarterly = pd.Series(data=data, index=dates)
quarterly

monthly = quarterly.asfreq('M') # to month-end frequency

# Fill Methods

# 1 - Forward Fill 
monthly['ffill'] = quarterly.asfreq('M', method='ffill')

# 2 - Backfill
monthly['bfill'] = quarterly.asfreq('M', method='bfill')

# 3 - Provide Value
monthly['value'] = quarterly.asfreq('M', fill_value = 0)

# Add missing months with .reindex()

dates = pd.date_range(start='2016', periods=12, freq='M')
quarterly.reindex(dates)

##############

# EXERCISE 1 - Convert monthly to weekly data

# Set start and end dates
start = '2016-1-1'
end = '2016-2-29'

# Create monthly_dates here
monthly_dates = pd.date_range(start=start, end=end, freq='M')

# Create monthly here
monthly = pd.Series(data=[1,2], index=monthly_dates)
print(monthly)

# Create weekly_dates here
weekly_dates = pd.date_range(start=start, end=end, freq='W')

# Print monthly, reindexed using weekly_dates
print(monthly.reindex(weekly_dates))
print(monthly.reindex(weekly_dates, method='bfill'))
print(monthly.reindex(weekly_dates, method='ffill'))

<script.py> output:
    2016-01-31    1
    2016-02-29    2
    Freq: M, dtype: int64
    2016-01-03    NaN
    2016-01-10    NaN
    2016-01-17    NaN
    2016-01-24    NaN
    2016-01-31    1.0
    2016-02-07    NaN
    2016-02-14    NaN
    2016-02-21    NaN
    2016-02-28    NaN
    Freq: W-SUN, dtype: float64
    2016-01-03    1
    2016-01-10    1
    2016-01-17    1
    2016-01-24    1
    2016-01-31    1
    2016-02-07    2
    2016-02-14    2
    2016-02-21    2
    2016-02-28    2
    Freq: W-SUN, dtype: int64
    2016-01-03    NaN
    2016-01-10    NaN
    2016-01-17    NaN
    2016-01-24    NaN
    2016-01-31    1.0
    2016-02-07    1.0
    2016-02-14    1.0
    2016-02-21    1.0
    2016-02-28    1.0
    Freq: W-SUN, dtype: float64

##############

# EXERCISE 2 - Create weekly from monthly unemployment data

# Import data here
data = pd.read_csv('unemployment.csv', parse_dates=['date'], index_col='date')

# Show first five rows of weekly series
print(data.asfreq('W').head())

# Show first five rows of weekly series with bfill option
print(data.asfreq('W', method='bfill').head())

# Create weekly series with ffill option and show first five rows
weekly_ffill = data.asfreq('W', method='ffill')
print(weekly_ffill.head())

# Plot weekly_fill starting 2015 here 
weekly_ffill.loc['2015':].plot()
plt.show()

<script.py> output:
                UNRATE
    date              
    2000-01-02     NaN
    2000-01-09     NaN
    2000-01-16     NaN
    2000-01-23     NaN
    2000-01-30     NaN
                UNRATE
    date              
    2000-01-02     4.1
    2000-01-09     4.1
    2000-01-16     4.1
    2000-01-23     4.1
    2000-01-30     4.1
                UNRATE
    date              
    2000-01-02     4.0
    2000-01-09     4.0
    2000-01-16     4.0
    2000-01-23     4.0
    2000-01-30     4.0


##############

# Upsampling & interpolation with .resample()

unrate = pd.read_csv('unrate.csv', parse_dates['Date'], index_col='Date')
unrate.info()
# no frequency information

# Resampling Period and Frequency Offsets

# Calendar Month-End - Alias: M
# Calendar Month-Start - Alias: MS
# Business Month-End - Alias: BM
# Business Month-Start - Alias: BMS

# Assign Frequency with .resample()

unrate.asfreq('MS').info()
unrate.resample('MS') # creates Resampler object

# Example with Quarterly real GDP growth

gdp = pd.read_csv('gdp,csv')
gdp.info()
# Data is reported for the 1st day of each quarter

# Use resample to convert this series to month-start frequency and forward fill to fill the gaps

gdp_1 = gdp.resample('MS').ffill().add_suffix('_ffill')

# Use interpolate to interpolate the missing values - finds points on straight line between existing data

gdp_2 = gdp.resample('MS').interpolate().add_suffix('_inter')

##############

# EXERCISE 1 - Use interpolation to create weekly employment data

# Inspect data here
print(monthly.info())

# Create weekly dates
weekly_dates = pd.date_range(monthly.index.min(), monthly.index.max(), freq='W')

# Reindex monthly to weekly data
weekly = monthly.reindex(weekly_dates)

# Create ffill and interpolated columns
weekly['ffill'] = weekly.UNRATE.ffill()
weekly['interpolated'] = weekly.UNRATE.interpolate()

# Plot weekly
weekly.plot()
plt.show()

# EXERCISE 2 - Interpolate debt/GDP and compare to unemployment

# Import & inspect data here
data = pd.read_csv('debt_unemployment.csv', parse_dates=['date'], index_col='date')
print(data.info())

# Interpolate and inspect here
interpolated = data.interpolate()
print(interpolated.info())

# Plot interpolated data here
interpolated.plot(secondary_y='Unemployment');
plt.show()

##############

# Downsampling & aggregation

ozone = pd.read_csv('ozone.csv', parse_dates=['date'], index_col='date')
# assign calendar day frequency
ozone = ozone.resample('D').asfreq()
ozone.info()

# apply monthly frequency with mean
ozone.resample('M').mean().head() # monthly frequency, assigned to end of a calendar month
# apply monthly frequency with median
ozone.resample('M').median().head()
# apply monthly frequency with aggregated method like groupby
ozone.resample('M').agg(['mean','std']).head()

# Plot the data starting 2016
ozone = ozone.loc['2016':]
ax = ozone.plot()
monthly = ozone.resample('M').mean()
monthly.add_suffix('_monthly').plot(ax=ax)

# Resample multiple time series

data = pd.read_csv('ozone_pm25.csv', parse_dates=['date'], index_col='date')
data = data.resample('D').asfreq()
data.info()

# business-month-end frequency
data = data.resample('BM').mean()
# month-end frequency
data = data.resample('M').first().head(4)
# month-start frequency
data = data.resample('MS').first().head()

##############

# EXERCISE 1 - Compare weekly, monthly and annual ozone trends for NYC & LA

# Import and inspect data here
ozone = pd.read_csv('ozone.csv', parse_dates=['date'], index_col='date')
ozone.info();

# Calculate and plot the weekly average ozone trend
ozone.resample('W').mean().plot();
plt.show()

# Calculate and plot the monthly average ozone trend
ozone.resample('M').mean().plot();
plt.show();

# Calculate and plot the annual average ozone trend
ozone.resample('A').mean().plot();
plt.show();


# EXERCISE 2 - Compare monthly average stock prices for Facebook and Google

# Import and inspect data here
stocks = pd.read_csv('stocks.csv', parse_dates=['date'], index_col='date')
print(stocks.info())

# Calculate and plot the monthly averages
monthly_average = stocks.resample('M').mean()
monthly_average.plot(subplots=True);
plt.show();

# EXERCISE 3 - Compare quarterly GDP growth rate and stock returns

# Import and inspect gdp_growth here
gdp_growth = pd.read_csv('gdp_growth.csv', parse_dates=['date'], index_col='date')
gdp_growth.info()

# Import and inspect djia here
djia = pd.read_csv('djia.csv', parse_dates=['date'], index_col='date')
djia.info()

# Calculate djia quarterly returns here 
djia_quarterly = djia.resample('QS').first()
djia_quarterly_return = djia_quarterly.pct_change().mul(100)

# Concatenate, rename and plot djia_quarterly_return and gdp_growth here 
data = pd.concat([gdp_growth, djia_quarterly_return], axis=1)
data.columns = ['gdp', 'djia']

data.plot()
plt.show();

# EXERCISE 4 - Visualize monthly mean, median and standard deviation of S&P500 returns

# Import data here
sp500 = pd.read_csv('sp500.csv', parse_dates=['date'], index_col='date')

# Calculate daily returns here
daily_returns = sp500.squeeze().pct_change()

# Resample and calculate statistics
stats = daily_returns.resample('M').agg(['mean', 'median','std'])

# Plot stats here
stats.plot()
plt.show()









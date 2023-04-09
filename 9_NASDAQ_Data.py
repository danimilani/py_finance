# WORKING WITH NASDAQ DATA IN PYTHON

# 1. Understanding your data

# Database: Month's worth of closing prices for Apple stock

aapl.head() # displays the first 5 rows
aapl.head(3) # displays the first 3 rows
aapl.tail() # displays the last 5 rows

# 2. Describe

aapl.describe() # returns summary statistics on all numerical columns - Statistical Summary of Data

# for numerical columns, it returns count, mean, std, min, percentiles and the max value
# arguments: include, exclude and percentiles

aapl.describe(include = 'object')
# different categories are returned depending on the column type
# object type returns count, unique, top and frequency

aapl.describe(include='all') # statistics are calculated for all the columns

# 3. Exclude

# Returns all column types except the specified

aapl.describe(exclude = 'float')

########################

# PRACTICE 

## Peek at top and bottom

# Peak at top five rows
alphabet.head()

""
                close        volume       open       high        low
date                                                                
2019/08/02  1196.3200  1745450.0000  1203.0000  1209.5000  1190.0000
2019/08/01  1211.7800  1771271.0000  1217.6300  1236.2980  1207.0000
2019/07/31  1218.2000  1997999.0000  1224.8700  1234.9100  1208.1800
2019/07/30  1228.0000  1430775.0000  1227.0000  1236.9100  1225.3200
2019/07/29  1241.8400  2069127.0000  1242.5000  1248.9950  1230.2000
""

# Peak at top seven rows.
alphabet.head(7)

"" 
                close        volume       open       high        low
date                                                                
2019/08/02  1196.3200  1745450.0000  1203.0000  1209.5000  1190.0000
2019/08/01  1211.7800  1771271.0000  1217.6300  1236.2980  1207.0000
2019/07/31  1218.2000  1997999.0000  1224.8700  1234.9100  1208.1800
2019/07/30  1228.0000  1430775.0000  1227.0000  1236.9100  1225.3200
2019/07/29  1241.8400  2069127.0000  1242.5000  1248.9950  1230.2000
2019/07/26  1245.2200  6060795.0000  1228.0000  1268.3940  1228.0000
2019/07/25  1135.9400  2738139.0000  1138.9500  1143.5910  1123.7100
""

# Peak at last row.
alphabet.tail(1)

""
               close        volume      open      high       low
date                                                            
2009/08/03  228.4316  2587139.0000  226.6787  229.2853  226.1231
""

## Describing data

# Get stats for all numeric columns
alphabet.describe()

""
          close     volume      open      high       low
count  2518.000  2.518e+03  2518.000  2518.000  2518.000
mean    612.300  2.278e+06   612.388   617.485   606.824
std     311.030  1.256e+06   310.957   313.721   308.055
min     220.279  5.211e+05   221.410   223.418   219.046
25%     309.344  1.519e+06   309.113   312.043   306.690
50%     550.888  1.977e+06   551.100   556.013   546.591
75%     830.720  2.619e+06   831.457   837.763   826.200
max    1296.200  1.480e+07  1289.120  1296.975  1271.710
""

# Get stats for integer columns only
alphabet.describe(include='int')

""
          volume
count  2.518e+03
mean   2.278e+06
std    1.256e+06
min    5.211e+05
25%    1.519e+06
50%    1.977e+06
75%    2.619e+06
max    1.480e+07
""

# Stats with percentiles for %30, %50, and %60
alphabet.describe(percentiles=[.3, .5, .6])

""
         close     volume      open      high       low
count  2518.000  2.518e+03  2518.000  2518.000  2518.000
mean    612.300  2.278e+06   612.388   617.485   606.824
std     311.030  1.256e+06   310.957   313.721   308.055
min     220.279  5.211e+05   221.410   223.418   219.046
30%     326.847  1.612e+06   326.648   329.874   323.824
50%     550.888  1.977e+06   551.100   556.013   546.591
60%     643.910  2.186e+06   644.414   654.982   633.561
max    1296.200  1.480e+07  1289.120  1296.975  1271.710
""

########################

# FILTERING DATA

prices.Symbol == 'AAPL'

# to return only data related to symbol AAPL
mask_symbol = prices.Symbol == 'AAPL'
aapl = prices.loc[mask_symbol]
aapl.describe(include='object') 

# returns values with the minimum of 2166
mask_high = [prices.High > 2160
big_price = prices.loc[mask_high]
big_price.describe()

# Boolean - AND (&), OR (|) and NOT(~)
             
# To get only the rows for non-Amazon stock later than April
             
# Condition 1
mask_prices = prices['Symbol']!='AMZN'
             
# Condition 2
mask_date = historical_highs['Date']>datetime(2020,4,1)

# Combine Conditions
mask_amzn = mask_prices & mask_date

# Run Argument to return results that matches both conditions
prices.loc[mask_amzn]             

########################

# PRACTICE 

## Filtering stock data

# Create a mask for all of the rows whose daily high is greater than $500.
# Create a DataFrame using this mask.

# Mask for large enough daily high
high_mask = alphabet.high > 500

# Filter using the mask
alphabet.loc[high_mask]

""
               close    volume      open      high       low
date                                                        
2019-08-02  1196.320   1745450  1203.000  1209.500  1190.000
2019-08-01  1211.780   1771271  1217.630  1236.298  1207.000
2019-07-31  1218.200   1997999  1224.870  1234.910  1208.180
2019-07-30  1228.000   1430775  1227.000  1236.910  1225.320
2019-07-29  1241.840   2069127  1242.500  1248.995  1230.200
...              ...       ...       ...       ...       ...
2013-10-24   518.051   2092054   521.244   525.639   517.673
2013-10-23   521.010   2663226   505.650   522.699   505.463
2013-10-22   508.681   2208639   507.671   511.712   503.019
2013-10-21   506.812   3628191   510.934   514.743   504.918
2013-10-18   510.908  11563920   493.314   512.955   492.011
""

# Create a mask for the volume of 1771271.
# Create a DataFrame of row(s) with a volume of 1771271.

# Mask for specific volume
volume_mask = alphabet.volume == 1771271

# Filter using the mask
alphabet.loc[volume_mask]

""
              close   volume     open      high     low
date                                                   
2019-08-01  1211.78  1771271  1217.63  1236.298  1207.0
""

# Make a mask for all rows where the volume does not equal 1997999.
# Filter using this mask.

# Mask rows whose volume is not 1997999
volume_mask = alphabet.volume != 1997999

# Filter using the mask
alphabet.loc[volume_mask]

""
               close   volume      open      high       low
date                                                       
2019-08-02  1196.320  1745450  1203.000  1209.500  1190.000
2019-08-01  1211.780  1771271  1217.630  1236.298  1207.000
2019-07-30  1228.000  1430775  1227.000  1236.910  1225.320
2019-07-29  1241.840  2069127  1242.500  1248.995  1230.200
2019-07-26  1245.220  6060795  1228.000  1268.394  1228.000
...              ...      ...       ...       ...       ...
2009-08-07   230.902  2540727   230.179   232.074   229.836
2009-08-06   227.497  2108417   229.487   229.780   226.573
2009-08-05   227.891  2340638   230.346   230.806   226.244
2009-08-04   229.201  2388618   226.997   229.336   226.522
2009-08-03   228.432  2587139   226.679   229.285   226.123
""

## Selecting data from data range

# Create a mask of historical dates in the given date range.
# A mask can be used to make a selection of rows from a DataFrame.

# Calculate the mask for one week
mask = (alphabet['date'] >= start_date) & (alphabet['date'] <= end_date)

# Use the mask to get the data for one week
df = alphabet[mask]

# Look at result
print(df)

""
         date      close        volume       open       high        low
1 2019-08-02  1196.3200  1745450.0000  1203.0000  1209.5000  1190.0000
2 2019-08-01  1211.7800  1771271.0000  1217.6300  1236.2980  1207.0000
3 2019-07-31  1218.2000  1997999.0000  1224.8700  1234.9100  1208.1800
4 2019-07-30  1228.0000  1430775.0000  1227.0000  1236.9100  1225.3200
5 2019-07-29  1241.8400  2069127.0000  1242.5000  1248.9950  1230.2000
""


########################

# PLOTTING DATA

# Core library is MatplotLib 

my_dataframe.plot()

# Line Plot - Default Plot Type Produced

exxon.plot(x='Date',
           y='High')


exxon.plot(x='Date',
           y='High'
          rot=90) # to rotate date labels by 90 degrees

exxon.plot(x='Date',
           y='High'
          rot=90
          title='Exxon Stock Price') # to add a title

 # If we leave out the x argument, the index is used for the x axis

exxon.set_index('Date', inplace=True)
exxon.plot(y='High',
           rot=90,
           title='Exxon Stock Price')

# Use the KIND parameter to change the plot type

exxon2018.plot(x='Month',
               y='Volume',
               kind='bar',
               title='Exxon 2018')

########################

# PRACTICE 

## Making a line plot

# Plot the daily high price
alphabet2w.plot(y = 'high')

# Plot the daily high price
alphabet2w.plot(y='high', rot=90) 

# Plot the daily high price
alphabet2w.plot(y='high', rot=90, title='High Daily Prices')

## Choose kind of plot

# Plot daily trade volume
alphabet2w.plot(y='volume', rot=90, title='Alphabet Daily Volume')

# Plot daily trade volume
alphabet2w.plot(y='volume', kind='bar', title='Alphabet Daily Volume')

# Plot daily trade volume
alphabet2w.plot(y='volume', kind='hist', title='Alphabet Daily Volume')


########################


# PANDAS DATAFRAMES

# CREATING DATA #

# Pandas is a 3rd party library

import pandas as pd

# Pandas DataFrame - it is very like a spreadsheet or table.
# Data labeled with columns and an index

pd.Dataframe()

# You can create empty DataFrames and populate it later
# The most common workflow is to pre-populate it with data when you create it

# 1. CREATING FROM DICT

data = {'Bank Code':['BA', 'AAD', 'BA'],
        'Account#': ['ajfdk2', '1234nmk', 'mm3d90'],
        'Balance':[1222.00, 390789.11, 13.02]}
# pass the dict to the DataFrame constructor using the data parameter
df = pd.DataFrame(data=dat)
# resulting DataFrame is: Dict Keys are used as column labels


# 2. CREATING FROM LIST OF DICTS

data = [{'Bank Code':'BA', 'Account#': 'ajfdk2', 'Balance':1222.00},
        {'Bank Code':'AAD', 'Account#': '1234nmk', 'Balance':390789.11}
        {'Bank Code':'BA', 'Account#': 'mm3d90', 'Balance':13.02}]
df = pd.DataFrame(data=data)
# resulting DataFrame is: Dict Keys are used as column labels


# 3. CREATING FROM LIST OF LISTS

data = [['BA', 'ajfdk2', 1222.00],
        ['AAD', '1234nmk', 390789.11],
        ['BA', 'mm3d90', 13.02]]
df = pd.DataFrame(data=data)
# The columns are given numerical names based on the position of the data in the lists

# 4. CREATING FROM LIST OF LISTS WITH COLUMN NAMES

data = [['BA', 'ajfdk2', 1222.00],
        ['AAD', '1234nmk', 390789.11],
        ['BA', 'mm3d90', 13.02]]
columns = ['Bank Code', 'Account#', 'Balance']
df = pd.DataFrame(data=data, columns=columns)

# 5. CREATING BY READING DATA FROM MANY DIFFERENT FORMATS

# Excel: pd.read_excel
# JSON: pd.read_json
# HTML: pd.read_html
# Pickle: pd.read_pickle
# SQL: pd.read_sql
# CSV: pd.read_csv

# Reading csv file

df = pd.read_csv('/data/daily/transactions.csv')

# Reading non-comma csv file

df = pd.read_csv('/data/daily/transactions.csv', sep='|')

################################################################

# EXERCISES #

## Creating DataFrames

# Create dict holding the data
data = {'Sym': ['APPL', 'APPL', 'APPL'],
        'Price': [105.00, 117.05, 289.80],
        'Date': ['2015/12/31', '2017/12/01', '2019/12/27']}

# Create DataFrame from the data
positions = pd.DataFrame(data=data)
print(positions)

<script.py> output:
        Sym   Price        Date
    0  APPL  105.00  2015/12/31
    1  APPL  117.05  2017/12/01
    2  APPL  289.80  2019/12/27

# Make list of dictionaries
data = [{'Sym': 'APPL', 'Price': 105.00, 'Date': '2015/12/31'},
        {'Sym': 'APPL', 'Price': 117.05, 'Date': '2017/12/01'},
        {'Sym': 'APPL', 'Price': 289.80, 'Date': '2019/12/27'}]

# Create DataFrame from the list
positions = pd.DataFrame(data=data)
print(positions)

<script.py> output:
        Sym   Price        Date
    0  APPL  105.00  2015/12/31
    1  APPL  117.05  2017/12/01
    2  APPL  289.80  2019/12/27

# Create a list of lists
data = [['APPL', 105.00, '2015/12/31'],
        ['APPL', 117.05, '2017/12/01'],
        ['APPL', 289.80, '2019/12/27']]

# Define the column names
columns = ['Sym', 'Price', 'Date']

# Create a DataFrame with the data and column names
df = pd.DataFrame(data=data, columns=columns)
print(df)

<script.py> output:
        Sym   Price        Date
    0  APPL  105.00  2015/12/31
    1  APPL  117.05  2017/12/01
    2  APPL  289.80  2019/12/27

## Reading market history

# Read the data
stocks = pd.read_csv('pcdg.csv')

# Look at the data
print(stocks)

<script.py> output:
                date      close        volume       open       high        low
    0          13:33   1,155.14     1,145,529      1,172   1,176.88      1,152
    1     2019/08/02  1196.3200  1745450.0000  1203.0000  1209.5000  1190.0000
    2     2019/08/01  1211.7800  1771271.0000  1217.6300  1236.2980  1207.0000
    3     2019/07/31  1218.2000  1997999.0000  1224.8700  1234.9100  1208.1800
    4     2019/07/30  1228.0000  1430775.0000  1227.0000  1236.9100  1225.3200
    ...          ...        ...           ...        ...        ...        ...
    2514  2009/08/07   230.9017  2540727.0000   230.1794   232.0737   229.8359
    2515  2009/08/06   227.4971  2108417.0000   229.4873   229.7803   226.5726
    2516  2009/08/05   227.8911  2340638.0000   230.3461   230.8058   226.2443
    2517  2009/08/04   229.2014  2388618.0000   226.9970   229.3358   226.5221
    2518  2009/08/03   228.4316  2587139.0000   226.6787   229.2853   226.1231
    
    [2519 rows x 6 columns]

################################################################

# ACCESSING DATA #

# Accessing Columns

# 1. Access column of the data

accounts['Balance']

# 2. Access column using dot-syntax

accounts.Balance

# 3. Access multiple columns at once

accounts[['Bank Code', 'Account#']]

# Accessing Rows

# 4. Access rows using brackets - slicing

accounts[0:2]

# 5. Access rows using brackets - boolean
# skipping middle row
accounts[[True, False, True]]

# LOC AND ILOC

# LOC - access by name

accounts.loc[['a','c']]
df.loc[[True, False, True]]

# columns with loc
accounts.loc['a':'c','Balance']

# ILOC - access by position - index and column positions

# Select first two rows using a slice and the first and last columns using a list
accounts.iloc[0:2, [0,2]]

# Setting Values

# 1. Setting a single value

accounts.loc['a', 'Balance'] = 0

# 2. Setting multiple values

# using slices of the first 2 rows and the last 2 columns and set cells to NA
accounts.iloc[:2, 1:] = 'NA'

################################################################

# EXERCISES #

## Accessing using names

# Select the Balance for October 2nd
print(ledger.loc['2020-10-02', 'Balance'])

# Select the Balance for October 3rd
print(ledger.loc['2020-10-03', 'Balance'])
<script.py> output:
    1322.0
    1922.0

# Cash and Securities for October 3rd
print(ledger.loc['2020-10-03', ['Cash', 'Securities']])
       
# Balance for October 1st and 3rd
print(ledger.loc[['2020-10-01','2020-10-03'] , 'Balance'])
<script.py> output:
        Cash         -100.0
Securities    700.0
Name: 2020-10-03, dtype: float64
2020-10-01    1222.0
2020-10-03    1922.0
Name: Balance, dtype: float64

# All columns for October 1st
print(ledger.loc['2020-10-01', :])

# Balance for all dates
print(ledger.loc[:, 'Balance'])
<script.py> output:
    Cash             0.0
    Securities    -300.0
    Balance       1222.0
    Name: 2020-10-01, dtype: float64
    2020-10-01    1222.0
    2020-10-02    1322.0
    2020-10-03    1922.0
    Name: Balance, dtype: float64

## Accessing using indexes

# Select the oldest price - Cell first row, Price column
print(positions.iloc[:1, 3:])

# Select the newest symbol - Cell last row, Symbol column
print(positions.iloc[2:, 0])
<script.py> output:
       Price
    0  96.96
    2    AMZN
    Name: Symbol, dtype: object

# Oldest two purchase dates
print(positions.iloc[0:2, 1])

# Newest purchase and quantity
print(positions.iloc[2, 1:3])

<script.py> output:
    0   2016-01-08
    1   2018-09-07
    Name: Purchased, dtype: datetime64[ns]
    Purchased    2020-02-14 00:00:00
    Quantity                      14
    Name: 2, dtype: object


# Set 2020 quantity
positions.iloc[2, 2] = 15

print(positions)
<script.py> output:
      Symbol  Purchased  Quantity   Price
    0   AAPL 2016-01-08        23   96.96
    1   AAPL 2018-09-07        50  221.30
    2   AMZN 2020-02-14        15  324.95

# Set all quantities to zero
positions.iloc[:3, 2] = 0

print(positions)
<script.py> output:
      Symbol  Purchased  Quantity   Price
    0   AAPL 2016-01-08         0   96.96
    1   AAPL 2018-09-07         0  221.30
    2   AMZN 2020-02-14         0  324.95

################################################################

# AGGREGATING AND SUMMARIZING DATA #

df.count() # counts the number of rows for each column
df.sum(axis=1)  # sums the values of all the columns of the 1st row
df.prod(axis='columns') # returns the product across columns
df.mean()
df.median() 
df.std() # standard deviation
df.var() # variance

# Select the maximum value from the column ADD
df.loc[:,'AAD'].max()

# Select minimum value from the 1st row
df.iloc[0].min()

################################################################

# EXERCISES #

## Median prices

# Get the median of the opening prices
med_open = prices.loc[:, 'OPEN'].median()

# Get the median of the closing prices
med_close = prices.loc[:, 'CLOSE'].median()

if med_open > med_close:
    print("Trending down.")

################################################################

# EXTENDING AND MANIPULATING DATA #


################################################################

# EXERCISES #

## Creating new columns

# Use the list pcesv to create the column PCESV
pce['PCESV'] = pcesv

# Use the DataFrame pcnd to create the column PCND
pce['PCND'] = pcnd

# Create column for PCDG using Pandas read_csv
pce['PCDG'] = pd.read_csv('pcdg.csv', index_col='DATE')

# Create a column PCE by adding values from other columns
pce['PCE'] = pce['PCDG'] + pce['PCND'] + pce['PCESV']
pce.head()

## Dropping columns from DataFrame

columns_to_drop = ['PCDG', 'PCND', 'PCESV']

# Print the current columns of the DataFrame pce
print(pce.columns)

# Create new_pce by dropping columns_to_drop from pce
new_pce = pce.drop(columns=columns_to_drop)
# Print the columns of the new DataFrame
print(new_pce.columns)

# Drop the columns in_place in the original DataFrame
pce.drop(columns=columns_to_drop, inplace=True)

# Print the columns of the DataFrame pce
print(pce.columns)
<script.py> output:
    Index(['PCDG', 'PCND', 'PCESV', 'PCE'], dtype='object')
    Index(['PCE'], dtype='object')
    Index(['PCE'], dtype='object')

## Manipulating data with Pandas

# Combine the source DataFrames into one
gdp = pd.concat([ge, gpdi, ne, pce], axis=1)

# Add the columns and create a new column with the result
gdp['GDP'] = gdp.apply(np.sum, axis=1)



################################################################

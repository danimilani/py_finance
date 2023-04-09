# PANDAS DATAFRAMES

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


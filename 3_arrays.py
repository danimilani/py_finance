# ARRAYS IN PYTHON

# PACKAGES - they are a colleaction of several Python scripts or modules introducing new 
# functions, methods and datatypes

# To install package

pip3 install package_name_here
pip3 install numpy

# You have to install it only once, but import it everytime you need to use it

import numpy

# NumPy and Arrays

import numpy
my_array = numpy.array([0,1,2,3,4])

print(my_array)
# result: [0,1,2,3,4]

print(type(my_array))
<class 'numpy.ndarray'>

# Using an Alias

import numpy as np
my_array = np.array([0,1,2,3,4])

# ARRAYS - more compact to store data, faster access to read/write, used with large datasets
# If you do create a numpy array with different data types as shown, NumPy will automatically
# convert all the elements to the most compatible type

my_array = np.array([3, 'is', True])
print(my_array)
# result: ['3', 'is', 'True'] - all elements are converted to a string

# ARRAY OPERATIONS

import numpy as np

array_A = np.array([1,2,3])
array_B = np.array([4,5,6])

print(array_A + array_B)
# result: [5 7 9]

# When you add two lists using the plus sign, the lists will be concatenated.
# When you add numpy arrays, the result is an element-wise sum of both the arrays

# ARRAY INDEXING

import numpy as np

months_array = np.array(['Jan', 'Feb', 'March', 'Apr', 'May'])

print(months_array[3])
# result: Apr

print(months_array[2:5])
# result: [March', 'Apr', 'May']

print(months_array[0:5:2])
['Jan' 'March' 'May']

##################################

# EXERCISES

# Import numpy as np
import numpy as np

# Lists
prices = [170.12, 93.29, 55.28, 145.30, 171.81, 59.50, 100.50]
earnings = [9.2, 5.31, 2.41, 5.91, 15.42, 2.51, 6.79]

# NumPy arrays
prices_array = np.array(prices)
earnings_array = np.array(earnings)

# Print the arrays
print(prices_array)
print(earnings_array)

<script.py> output:
    [170.12  93.29  55.28 145.3  171.81  59.5  100.5 ]
    [ 9.2   5.31  2.41  5.91 15.42  2.51  6.79]

# Elementwise operations on arrays

# Import numpy as np
import numpy as np

# Create PE ratio array
pe_array = (prices_array/earnings_array)

# Print pe_array
print(pe_array)

<script.py> output:
    [18.49130435 17.56873823 22.93775934 24.58544839 11.14202335 23.70517928
     14.8011782 ]

# Subsetting elements from an array

# Subset the first three elements from prices_array.

# Subset the first three elements
prices_subset_1 = prices_array[0:3]
print(prices_subset_1)

<script.py> output:
    [170.12  93.29  55.28]

# Subset the last three elements from the prices_array using negative index slicing.

# Subset last three elements 
prices_subset_2 = prices_array[-3:]
print(prices_subset_2)

<script.py> output:
    [171.81  59.5  100.5 ]

# Subset every third element from the prices_array using step slicing.

# Subset every third element
prices_subset_3 = prices_array[0:7:3]
print(prices_subset_3)

<script.py> output:
    [170.12 145.3  100.5 ]
    
##################################

# 2 Dimensional arrays and functions

# Often financial or quantitative data comes in the form of a table, with rows and columns
# To create a 2D array in Python, instead of providing a single list as the input
# you pass in a list of two lists as the input as shown here

import numpy as np
months = [1,2,3]
prices = [238.11, 237.81, 238.91]

cpi_array = np.array([months, prices])
print(cpi_array)

# result:  [[ 1 2 3] 
[238.11 237.81 238.91]]

# .shape gives you dimensions of the array - rows and columns
print(cpi_array.shape)
# result: (2,3)

# .size gives you the total number of elements in the array
print(cpi_array.size)
# result: 6

# .np.mean() calculates the mean of an input
print(np.mean(prices_array))
# result: 238.2766666667

# .np.std() calculates the standard deviation of an input
print(np.std(prices_array))
# result: 0.464279609

# Function 'arange()'
# It creates an array with start, end, step

import numpy as np
months = np.arange(1,13)
print(months)
[1 2 3 4 5 6 7 8 9 10 11 12]

months_odd = np.arange(1,13,2)
print(months_odd)
[1 3 5 7 9 11]

# Function 'transpose()'
# It switches rows and column of a numpy array

print(cpi_array)
[[ 1 2 3 ]
 [238.11 237.81 238.91]]

cpi_transposed = np.transpose(cpi_array)
print(cpi_transposed)

[[1 238.11]
 [2 237.81]
 [3 238.91]]

# Array indexing for 2D arrays

print(cpi_array)
[[ 1 2 3]
 [ 238.11 237.81 238.91]]

# row index 1, column index 2
cpi_array[1,2]
# result: 238.91

# all row slice, third column
print(cpi_array[:,2])
[ 3 238.91]

##################################

# EXERCISE

# Creating a 2D array

# Create a two dimensional array of prices and earnings (in that order) and assign it to stock_array.

# Create a 2D array of prices and earnings
stock_array = np.array([prices, earnings])
print(stock_array)

# Print the shape of stock_array
print(stock_array.shape)

# Print the size of stock_array
print(stock_array.size)

<script.py> output:
    [[170.12  93.29  55.28 145.3  171.81  59.5  100.5 ]
     [  9.2    5.31   2.41   5.91  15.42   2.51   6.79]]
    (2, 7)
    14

# Transpose stock_array and assign the result to stock_array_transposed.

# Transpose stock_array
stock_array_transposed = np.transpose(stock_array)
print(stock_array_transposed)

# Print the shape of stock_array
print(stock_array_transposed.shape)

# Print the size of stock_array
print(stock_array_transposed.size)

<script.py> output:
    [[170.12   9.2 ]
     [ 93.29   5.31]
     [ 55.28   2.41]
     [145.3    5.91]
     [171.81  15.42]
     [ 59.5    2.51]
     [100.5    6.79]]
    (7, 2)
    14

# Subsetting 2D arrays

# Extract the first column from stock_array_transposed and assign it to prices.

# Subset prices from stock_array_transposed
prices = stock_array_transposed[:, 0]
print(prices)

<script.py> output:
    [170.12  93.29  55.28 145.3  171.81  59.5  100.5 ]

# Extract the second column from stock_array_transposed and assign it to earnings.

# Subset earnings from stock_array_transposed
earnings = stock_array_transposed[:,1]
print(earnings)

<script.py> output:
    [ 9.2   5.31  2.41  5.91 15.42  2.51  6.79]

# Subset the price and earning of the first company (row 0) from stock_array_transposed and assign it to company_1.

# Subset the price and earning for first company
company_1 = stock_array_transposed[0,:]
print(company_1)

<script.py> output:
    [170.12   9.2 ]

# Calculating array stats

# Calculate the mean of prices.

# Calculate the mean 
prices_mean = np.mean(prices)
print(prices_mean)

<script.py> output:
    113.6857142857143

# Calculate the standard deviation of prices.

# Calculate the standard deviation 
prices_std = np.std(prices)
print(prices_std)

<script.py> output:
    45.51277932221513

# Generating a sequence of numbers

# Create an array company_ids containing the numbers 1 through 7 (inclusive).
# Create an array company_ids_odd containing only the odd numbers from 1 through 7 (inclusive).

# Create and print company IDs
company_ids = np.arange(1, 8, 1)
print(company_ids)

# Use array slicing to select specific company IDs
company_ids_odd = np.arange(1, 8, 2)
print(company_ids_odd)

<script.py> output:
    [1 2 3 4 5 6 7]
    [1 3 5 7]

##################################

# Using arrays for analysis

# Find elements in prices that are greater than price_mean and assign the boolean result to boolean_array.
# Subset prices using boolean_array and assign the result to above_avg.

# Find the mean
price_mean = np.mean(prices)

# Create boolean array
boolean_array = (prices > price_mean)
print(boolean_array)

# Select prices that are greater than average
above_avg = prices[boolean_array]
print(above_avg)

<script.py> output:
    [ True False False  True  True False False]
    [170.12 145.3  171.81]

# Find elements in sectors that are equivalent to 'Health Care' and assign the result to boolean_array.
# Subset names using boolean_array and assign the result to health_care.

# Create boolean array
boolean_array = (sectors == 'Health Care')
print(boolean_array)

# Print only health care companies
health_care = names[boolean_array]
print(health_care)

<script.py> output:
    [False  True  True False  True]
    ['Abbvie Inc' 'Abbott Laboratories' 'Allergan Plc']





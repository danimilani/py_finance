# LISTS IN PYTHON

# Lists - Square Brackets with zero-index

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dec']

# To access an element of a list, you can use the integer representing the index position
# inside square brackets

months[0]

# Result: 'Jan'

# Negative index can be used to start counting from the end of the list

months[-1]

# Result: 'Dec'

# SLICING - subsetting multiple list elements from a list
# Includes the start and up to (but not including) the end

mylist[startAt:endBefore]

months = ['January', 'February', 'March', 'April', 'May', 'June']

months[2:5]

# Result: ['March', 'April', 'May']

# Negative Indexing

months[-4:-1]

# Result: ['March', 'April', 'May']

# Extended Slicing

months[3:]
# Result: ['April', 'May', 'June']

months[:3]
# Result: ['January', 'February', 'March']

# Slicing with Steps

# Includes the start and up to (but not including) the end

mylist[startAt:endBefore:step]

# The step is an integer value which determines the increment between each index for slicing
# If the step is not explicitly provided, it is 1 by default.

months = ['January', 'February', 'March', 'April', 'May', 'June']

months[0:6:2]
# Result: ['January', 'March', 'May']

months[0:6:3]
# Result: ['January', 'April']


#####################

# EXERCISES

# Creating lists in Python

# Create a list named names containing the strings 'Apple Inc', 'Coca-Cola', and 'Walmart', in that order.

# Create and print list names
names = ['Apple Inc', 'Coca-Cola', 'Walmart']
print(names)

# Create and print list prices
prices = [159.54, 37.13, 71.17]
print(prices)

# Results

['Apple Inc', 'Coca-Cola', 'Walmart']
[159.54, 37.13, 71.17]

#####################

# Indexing list items


# Print the first item in names
print(names[0])

# Print the second item in names
print(names[1])

# Print the last element in prices
print(prices[-1])

<script.py> output:
    Apple Inc
    Coca-Cola
    71.17
    
#####################

# Slicing multiple list elements

# Use list slicing to subset the last two elements from names.

# names
names = ['Apple Inc', 'Coca-Cola', 'Walmart']

# Use slicing on list names
names_subset = names[1:]
print(names_subset)

<script.py> output:
    ['Coca-Cola', 'Walmart']
    
# Use extended slicing and specifying appropriate indices to subset the first two elements from prices.

# prices
prices = [159.54, 37.13, 71.17]

# Use extended slicing on the list prices
prices_subset = prices[0:2]
print(prices_subset)

<script.py> output:
    [159.54, 37.13]

#####################

# NESTED LISTS

# Lists that contain other lists

cpi = [['Jan', 'Feb', 'Mar'], [238.11,237.81,238.91]]

# Subsetting Nested Lists

cpi = [['Jan', 'Feb', 'Mar'], [238.11,237.81,238.91]]
print(cpi[1])
# Result: [238.11,237.81,238.91]

cpi = [['Jan', 'Feb', 'Mar'], [238.11,237.81,238.91]]
print(cpi[1][0])
# Result: 238.11

#####################

# Execises

# Stock up a nested list

# Create and print the nested list stocks
stocks = [names, prices]
print(stocks)

# Use list indexing to obtain the list of prices
print(stocks[1])

<script.py> output:
    [['Apple Inc', 'Coca-Cola', 'Walmart'], [159.54, 37.13, 71.17]]
    [159.54, 37.13, 71.17]

# Subset a nested list

# Use indexing to obtain company name Coca-Cola
print(stocks[0][1])

# Use indexing to obtain 71.17
print(stocks[1][2])

#####################

# LIST METHODS AND FUNCTIONS

# FUNCTIONS take objects as inputs or are passed an object
# Example: type(prices)

# METHODS act on objects
# Example: prices.sort()

# METHODS

# APPEND - adds a single element to a list, at the end of the list
months = ['January', 'February', 'March']
months.append('April')
print(months)
# result: ['January', 'February', 'March', 'April']

# EXTEND - adds multiple elemets to a list
months.extend(['May', 'June', 'July']
print(months)
# result: ['January', 'February', 'March', 'April', 'May', 'June', 'July']

# INDEX - returns the index of an specific element
months = ['January', 'February', 'March']
prices = [238.11,237.81,238.91]

months.index('February')
# result: 1

print(prices[1])
# result: 237.81

# FUNCTIONS

# MIN(list) - identify the min element of a list
# MAX(list) - identify the max element of a list

# Example

# Identify min price
min_price = min(prices)
# Identify min price index
min_index = prices.index(min_price)
# Identify the month with min price
min_month = months[min_index]
print(min_month)

# Result: February

#####################

# EXERCISES

# Exploring list methods and functions

# Using the method .sort(), sort and print the prices in the list prices.

# Print the sorted list prices
prices = [159.54, 37.13, 71.17]
prices.sort()
print(prices)
# result: [37.13, 71.17, 159.54]

# Identify the maximum price in prices using the function max().

# Find the maximum price in the list price
prices = [159.54, 37.13, 71.17]
price_max = max(prices)
print(price_max)
# result: 159.54

# Using list methods to add data

# Append a name to the list names
names.append('Amazon.com')
print(names)

# Extend list names
more_elements = ['DowDuPont', 'Alphabet Inc']
names.extend(more_elements)
print(names)

['Apple Inc', 'Coca-Cola', 'Walmart', 'Amazon.com']
['Apple Inc', 'Coca-Cola', 'Walmart', 'Amazon.com', 'DowDuPont', 'Alphabet Inc']

# Finding stock with maximum price

# Do not modify this
max_price = max(prices)

# Identify index of max price
max_index = prices.index(max_price)

# Identify the name of the company with max price
max_stock_name = names[max_index]

# Fill in the blanks 
print('The largest stock price is associated with ' + max_stock_name + ' and is $' + str(max_price) + '.')

# result: The largest stock price is associated with Amazon.com and is $1705.54.







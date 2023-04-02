# Introduction to Python for Finance

# Exercise 1 - Running Codes

# Create the variable total and print the total revenue
total = (revenue_1+revenue_2+revenue_3)
print(total)

# Print the average revenue
average = total/3
print(average)

# Data Types

# Strings, Integers, Floats and Booleans

print(type(variable_name))

# Boolean
print(1 == 1)
# result is true
# type is bool = boolean

# Variable Manipulations

x = 5
print(x*3)
# result is 15

y = 'stock'
print(y*3)
# result is 'stockstockstock'


x = 5
print(x+3)
# result is 8

y = 'stock'
print(y+3)
# result is TypeError: must be str, not int

# Exercise 2

# Creating Variables

# Create company_1
company_1 = 'Apple'
print(company_1)

# Create year_1
year_1 = 2017
print(year_1)

# Create revenue_1
revenue_1 = 229.23
print(revenue_1)

# Data Types

# Type of company_1
print(type(company_1))

# Type of year_1
print(type(year_1))

# Type of revenue_1
print(type(revenue_1))

<script.py> output:
    <class 'str'>
    <class 'int'>
    <class 'float'>

# Booleans

# The name of company 1 is provided as company_1. 
# Determine if the variable test_company is equivalent to company_1.

# Test equality
test_company = 'apple'
print(company_1 == test_company)

# Result = false

# The revenue of company 1 and company 2 are provided as revenue_1 and revenue_2, respectively.
# Using a comparison operator, determine if revenue_1 is greater than revenue_2.

# Compare revenue_1 and revenue_2
print(revenue_1 > revenue_2)

# result = True

# Combining Data Types

# Different types of data types have different properties. 
# For example, strings and floats cannot be mathematically combined. 
# To convert a variable x to an integer, you can use the command int(x). 
# Similarly, to convert a variable y to a string, you can use the command str(y).

# Update data types
year_1_str = str(year_1)
revenue_1_str = str(revenue_1)

# Create a complete sentence combining only the string data types
sentence = 'The revenue of ' + company_1 + ' in ' + year_1_str + ' was $' + revenue_1_str + ' billion.'

# Print sentence
print(sentence)

# Result: The revenue of Apple in 2017 was $229.23 billion.






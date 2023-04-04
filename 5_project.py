## Project  S&P 100

# First four items of names
print(names[0:4])

# Print information on last company
print(names[-1])
print(prices[-1])
print(earnings[-1])
print(sectors[-1])

# Import numpy as np
import numpy as np

# Convert lists to arrays
prices_array = np.array(prices)
earnings_array = np.array(earnings)

# Calculate P/E ratio 
pe = prices_array/earnings_array
print(pe)

# Create boolean array 
boolean_array = (sectors == 'Information Technology')

# Subset sector-specific data
it_names = names[boolean_array]
it_pe = pe[boolean_array]

# Display sector names
print(it_names)
print(it_pe)

"""
<script.py> output:
    ['Apple Inc' 'Accenture Plc' 'Cisco Systems Inc' 'Facebook Inc'
     'Alphabet Class C' 'Alphabet Class A' 'International Business Machines'
     'Intel Corp' 'Mastercard Inc' 'Microsoft Corp' 'Oracle Corp'
     'Paypal Holdings' 'Qualcomm Inc' 'Texas Instruments' 'Visa Inc']
    [18.49130435 24.58544839 16.76497696 34.51637765 34.09708738 34.6196853
     11.08345534 14.11320755 34.78654292 24.40532544 19.20392157 54.67857143
     17.67989418 24.28325123 31.68678161]
"""

# Create boolean array 
boolean_array = (sectors == 'Consumer Staples')

# Subset sector-specific data
cs_names = names[boolean_array]
cs_pe = pe[boolean_array]

# Display sector names
print(cs_names)
print(cs_pe)

"""
<script.py> output:
   ['Colgate-Palmolive Company' 'Costco Wholesale' 'CVS Corp'
     'Kraft Heinz Co' 'Coca-Cola Company' 'Mondelez Intl Cmn A' 'Altria Group'
    'Pepsico Inc' 'Procter & Gamble Company'
     'Philip Morris International Inc' 'Walgreens Boots Alliance'
     'Wal-Mart Stores']
    [25.14285714 29.41924399 12.29071804 22.63764045 24.12698413 20.72682927
     21.04746835 22.55859375 22.19346734 23.01781737 13.7745098  22.03669725]
"""

# Calculate mean and standard deviation
it_pe_mean = np.mean(it_pe)
it_pe_std = np.std(it_pe)

print(it_pe_mean)
print(it_pe_std)

"""
26.333055420408595
10.8661467926753
"""

# Calculate mean and standard deviation
cs_pe_mean = np.mean(cs_pe)
cs_pe_std = np.std(cs_pe)

print(cs_pe_mean)
print(cs_pe_std)

"""
21.581068906419564
4.412021654267338
"""

# Plot PE Ratios

import matplotlib.pyplot as plt

# Make a scatterplot
plt.scatter(it_id, it_pe, color='red', label='IT')
plt.scatter(cs_id, cs_pe, color='green', label='CS')

# Add legend
plt.legend()

# Add labels
plt.xlabel('Company ID')
plt.ylabel('P/E Ratio')
plt.show()

# Histogram of P/E ratios

# Import matplotlib.pyplot with the alias plt
import matplotlib.pyplot as plt

# Plot histogram 
plt.hist(it_pe, bins=8)

# Add x-label
plt.xlabel('P/E ratio')

# Add y-label
plt.ylabel('Frequency')

# Show plot
plt.show()

# Name the outlier

# Identify P/E ratio within it_pe that is > 50
outlier_price = it_pe[it_pe > 50]

# Identify the company with PE ratio > 50
outlier_name = it_names[it_pe > 50]

# Display results
print("In 2017, " + str(outlier_name[0]) + " had an abnormally high P/E ratio of " + str(round(outlier_price[0], 2)) + ".")

"""
<script.py> output:
    In 2017, Paypal Holdings had an abnormally high P/E ratio of 54.68.
"""



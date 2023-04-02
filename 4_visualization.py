# VISUALIZATION IN PYTHON

# Matplotlib is the most famous package
# matplotlib.pyplot - diverse plotting functions

import matplotlib.pyplot as plt

# plt.plot() - takes arguments that describe the data to be plotted
# plt.show() - displays plot to screen

# Plotting with pyplot

import matplotlib.pyplot as plt
plt.plot(months, prices)
plt.show()

# Customizing the Plot

import matplotlib.pyplot as plt
plt.plot(months, prices, color = 'red')
plt.show()

import matplotlib.pyplot as plt
plt.plot(months, prices, color = 'red', linestyle = '--')
plt.show()

# Adding Labels and Titles

import matplotlib.pyplot as plt
plt.plot(months, prices, color = 'red', linestyle = '--')
plt.show()

# Add Labels
plt.xlabel('Months')
plt.ylabel('Consumer Price Indexes, $')
plt.title('Average Monthly Consumer Price Indexes')

# Show Plot
plt.show()

# Adding Additional Lines

import matplotlib.pyplot as plt
plt.plot(months, prices, color = 'red', linestyle = '--')
# adding additional line
plt.plot(months, prices_new, color = 'green', linestyle = '--')
plt.xlabel('Months')
plt.ylabel('Consumer Price Indexes, $')
plt.title('Average Monthly Consumer Price Indexes')
plt.show()

# Scatterplots

import matplotlib.pyplot as plt
plt.scatter(x = months, y = prices, color = 'red')
plt.show()

######################################

# EXERCISE

# Importing matplotlib and pyplot

# Import matplotlib.pyplot with the alias plt
import matplotlib.pyplot as plt

# Plot the price of stock over time
plt.plot(days, prices, color="red", linestyle="--")

# Display the plot
plt.show()

# Adding axis labels and titles

import matplotlib.pyplot as plt

# Plot price as a function of time
plt.plot(days, prices, color="red", linestyle="--")

# Add x and y labels
plt.xlabel('Days')
plt.ylabel('Prices, $')

# Add plot title
plt.title('Company Stock Prices Over Time')

# Show plot
plt.show()

# Multiple lines on the same plot

# Plot two lines of varying colors 
plt.plot(days, prices1, color='red')
plt.plot(days, prices2, color='green')

# Add labels
plt.xlabel('Days')
plt.ylabel('Prices, $')
plt.title('Stock Prices Over Time')
plt.show()

# Scatterplots

# Import pyplot as plt
import matplotlib.pyplot as plt

# Plot price as a function of time
plt.scatter(days, prices, color='green', s=0.1)

# Show plot
plt.show()

######################################

# HISTOGRAMS

# Common graph used to display data as they tell the distribution of the data

import matplotlib.pyplot as plt
plt.hist(x=prices, bins=3)
plt.show()

# When there are more bins, the number of obs in each bin decreases

import matplotlib.pyplot as plt
plt.hist(x=prices, bins=6)
plt.show()

# Normalizing histogram data

import matplotlib.pyplot as plt
plt.hist(x=prices, bins=6, normed=1)
plt.show()

# Layering histograms on a plot

import matplotlib.pyplot as plt
plt.hist(x=prices, bins=6, normed=1)
plt.hist(x=prices_new, bins=6, normed=1)
plt.show()

# Alpha: Changing the transparency of histograms

import matplotlib.pyplot as plt
plt.hist(x=prices, bins=6, normed=1, alpha=0.5)
plt.hist(x=prices_new, bins=6, normed=1, alpha=0.5)
plt.show()

# Adding a legend
import matplotlib.pyplot as plt
plt.hist(x=prices, bins=6, normed=1, alpha=0.5, label='Prices 1')
plt.hist(x=prices_new, bins=6, normed=1, alpha=0.5, label='Prices New')
plt.show()

######################################

# EXERCISES

## Is data normally distributed?

# Plot histogram 
plt.hist(prices, bins=100)

# Display plot
plt.show()

## Comparing two histograms

# Plot histogram of stocks_A
plt.hist(stock_A, bins=100, alpha=0.4)

# Plot histogram of stocks_B 
plt.hist(stock_B, bins=100, alpha=0.4)

# Display plot
plt.show()

## Adding a legend

# Plot stock_A and stock_B histograms
plt.hist(stock_A, bins=100, alpha=0.4, label='Stock A')
plt.hist(stock_B, bins=100, alpha=0.4, label='Stock B')

# Add the legend
plt.legend()

# Display the plot
plt.show()



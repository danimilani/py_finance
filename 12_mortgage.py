## MORTGAGE BASICS

# You can use numpy function .pmt(rate,nper,pv) to compute the periodic mortgage loan payment.

# EXAMPLE
# Calculate the monthly mortgage payment of a 400,000$ 30y loan at 3.8% interest:

import numpy as np
monthly_rate = ((1+0.038)**(1/12)-1)
np.pmt(rate=monthly_rate, nper=12*30, pv=400000)
#result: -1849.15

# EXERCISE - Taking out a mortgage loan

import numpy as np

# Set the value of the home you are looking to buy
home_value = 800000

# What percentage are you paying up-front?
down_payment_percent = 0.20

# Calculate the dollar value of the down payment
down_payment = (home_value*down_payment_percent)
print("Initial Down Payment: " + str(down_payment))

# Calculate the value of the mortgage loan required after the down payment
mortgage_loan = home_value - down_payment
print("Mortgage Loan: " + str(mortgage_loan))

#Initial Down Payment: 160000.0
#Mortgage Loan: 640000.0

# EXERCISE - Calculating the monthly mortgage payment

import numpy as np

# Derive the equivalent monthly mortgage rate from the annual rate
mortgage_rate_periodic = ((1+0.0375)**(1/12)-1)

# How many monthly payment periods will there be over 30 years?
mortgage_payment_periods = 12*30

# Calculate the monthly mortgage payment (multiply by -1 to keep it positive)
periodic_mortgage_payment = -1*np.pmt(rate=mortgage_rate_periodic, nper=mortgage_payment_periods, pv=mortgage_loan)

print("Monthly Mortgage Payment: " + str(round(periodic_mortgage_payment, 2)))
#Result: Monthly Mortgage Payment: 2941.13

## Amortization, interest and principal

## Accumulating values via for loops in Python

accumulator = 0
for i in range(3):
  if i == 0:
    accumulator = accumulator + 3
  else:
    accumulator = accumulator + 1
  print(str(i)+": Loop value: "+str(accumulator))
  
## EXERCISE - Calculating interest and principal payments

# Calculate the amount of the first loan payment that will go towards interest
initial_interest_payment = mortgage_loan*mortgage_rate_periodic
print("Initial Interest Payment: " + str(round(initial_interest_payment, 2)))

# Calculate the amount of the first loan payment that will go towards principal
initial_principal_payment = periodic_mortgage_payment - initial_interest_payment
print("Initial Principal Payment: " + str(round(initial_principal_payment, 2)))

#Initial Interest Payment: 1966.43
#Initial Principal Payment: 974.7

# EXERCISE - Simulating periodic payments (I)

# Loop through each mortgage payment period
for i in range(0, mortgage_payment_periods):
    
    # Handle the case for the first iteration
    if i == 0:
        previous_principal_remaining = mortgage_loan
    else:
        previous_principal_remaining = principal_remaining[i-1]
        
    # Calculate the interest and principal payments
    interest_payment = round(previous_principal_remaining*mortgage_rate_periodic, 2)
    principal_payment = round(periodic_mortgage_payment - interest_payment, 2)
    
    # Catch the case where all principal is paid off in the final period
    if previous_principal_remaining - principal_payment < 0:
        principal_payment = previous_principal_remaining
        
    # Collect the principal remaining values in an array
    principal_remaining[i] = previous_principal_remaining - principal_payment
    
    # Print the payments for the first few periods
    print_payments(i, interest_payment, principal_payment, principal_remaining)

#Period 0: Interest Paid: 1966.43 | Principal Paid: 974.7 | Remaining Balance: 639025.3
#Period 1: Interest Paid: 1963.43 | Principal Paid: 977.7 | Remaining Balance: 638047.6000000001
#Period 2: Interest Paid: 1960.43 | Principal Paid: 980.7 | Remaining Balance: 637066.9000000001
#Period 3: Interest Paid: 1957.41 | Principal Paid: 983.72 | Remaining Balance: 636083.1800000002
#Period 4: Interest Paid: 1954.39 | Principal Paid: 986.74 | Remaining Balance: 635096.4400000002
#Period 5: Interest Paid: 1951.36 | Principal Paid: 989.77 | Remaining Balance: 634106.6700000002

# Simulating periodic payments (II)

# Loop through each mortgage payment period
for i in range(0, mortgage_payment_periods):
    
    # Handle the case for the first iteration
    if i == 0:
        previous_principal_remaining = mortgage_loan
    else:
        previous_principal_remaining = principal_remaining[i-1]
        
    # Calculate the interest based on the previous principal
    interest_payment = round(previous_principal_remaining*mortgage_rate_periodic, 2)
    principal_payment = round(periodic_mortgage_payment - interest_payment, 2)
    
    # Catch the case where all principal is paid off in the final period
    if previous_principal_remaining - principal_payment < 0:
        principal_payment = previous_principal_remaining
        
    # Collect the historical values
    interest_paid[i] = interest_payment
    principal_paid[i] = principal_payment
    principal_remaining[i] = previous_principal_remaining - principal_payment
    
# Plot the interest vs principal
plt.plot(interest_paid, color="red")
plt.plot(principal_paid, color="blue")
plt.legend(handles=[interest_plot, principal_plot], loc=2)
plt.show()

# Home ownership, equity and forecasting

# Cumulative Operations in NumPy

##Cumulative SUM
import numpy as np
np.cumsum(np.array([1,2,3]))

## Cumulative Product
import numpy as np
np.cumprod(np.array[1,2,3]))

# Forecasting cumulative growth

# EXAMPLE: What is the cumulative value at each point in time of a $100 investment 
#that grows by 3% in p1, 3% in p2, and 5% in p3?

import numpy as np
np.cumprod(1 + np.array([0.03, 0.03, 0.05]))
#result: array([1.03, 1.0609, 1.113945])

# EXERCISE - Cumulative payments and home equity

import numpy as np

# Calculate the cumulative home equity (principal) over time
cumulative_home_equity = np.cumsum(np.array([principal_paid]))

# Calculate the cumulative interest paid over time
cumulative_interest_paid = np.cumsum(np.array([interest_paid]))

# Calculate your percentage home equity over time
cumulative_percent_owned = down_payment_percent + (cumulative_home_equity/home_value)
print(cumulative_percent_owned)

# Plot the cumulative interest paid vs equity accumulated
plt.plot(cumulative_interest_paid, color='red')
plt.plot(cumulative_home_equity, color='blue')
plt.legend(handles=[interest_plot, principal_plot], loc=2)
plt.show()

# EXERCISE - Rising housing prices

import numpy as np

# Calculate the cumulative growth over time
cumulative_growth_forecast = np.cumprod(1+growth_array)

# Forecast the home value over time
home_value_forecast = home_value*cumulative_growth_forecast

# Forecast the home equity value owned over time
cumulative_home_value_owned = cumulative_percent_owned*home_value_forecast

# Plot the home value vs equity accumulated
plt.plot(home_value_forecast, color='red')
plt.plot(cumulative_home_value_owned, color='blue')
plt.legend(handles=[homevalue_plot, homeequity_plot], loc=2)
plt.show()

# EXERCISE - Falling housing prices and underwater mortgages

# An underwater mortgage is when the remaining amount you owe on your mortgage 
# is actually higher than the value of the house itself.

# In this exercise, you will calculate the worst case scenario where home prices 
# drop steadily at the rate of 0.45% per month.

import numpy as np
import pandas as pd

# Cumulative drop in home value over time as a ratio
cumulative_decline_forecast = np.cumprod(1+decline_array)

# Forecast the home value over time
home_value_forecast = cumulative_decline_forecast * home_value

# Find all periods where your mortgage is underwater
underwater = principal_remaining > home_value_forecast
pd.value_counts(underwater)

# Plot the home value vs principal remaining
plt.plot(home_value_forecast, color='red')
plt.plot(principal_remaining, color='blue')
plt.legend(handles=[homevalue_plot, principal_plot], loc=2)
plt.show()






# BUDGETING APPLICATION

# Budgeting project proposal

# Constant cumulative growth forecast

## What is the cumulative growth of an investment that grows by 3% py for 3y?
import numpy as np
np.cumprod(1 + np.repeat(0.03, 3))-1
#result: array([0.03,0.0609, 0.0927])

##Compute the value at each point in time of an initial $100 investment that
#grows by 3%py for 3years?
import numpy as np
100 * np.cumprod(1+np.repeat(0.03,3))
#result: array([103,106.909,109.27])

# BUDGETING APPLICATION EXERCISES

# 1. SALARY AND TAXES

#Assume a 30% tax rate and a base salary of $85,000.
#Calculate your take home salary after taxes.
#Calculate your monthly salary after taxes 

# Enter your annual salary
salary = 85000

# Assume a tax rate of 30%
tax_rate = 0.30

# Calculate your salary after taxes
salary_after_taxes = salary * (1-tax_rate)
print("Salary after taxes: " + str(round(salary_after_taxes, 2)))

# Calculate your monthly salary after taxes
monthly_takehome_salary = salary_after_taxes / 12
print("Monthly takehome salary: " + str(round(monthly_takehome_salary, 2)))

#Salary after taxes: 59500.0
#Monthly takehome salary: 4958.33

# 2. MONTHLY EXPENSES AND SAVINGS

#Rent: $1200 / month (Includes utilities)
#Food: $30 / day (On average. Includes groceries and eating out.)
#Entertainment: $200 / month (Movies, drinks, museums, parties…)
#Unforeseen Expenses: 250 / month (Stay safe, and don't drop your phone!)
#For this application, assume an average of 30 days per month.

# Enter your monthly rent
monthly_rent = 1200

# Enter your daily food budget
daily_food_budget = 30

# Calculate your monthly food budget assuming 30 days per month
monthly_food_budget = 30*30

# Set your monthly entertainment budget
monthly_entertainment_budget = 200

# Allocate funds for unforeseen expenses, just in case
monthly_unforeseen_expenses = 250

# Next, calculate your total monthly expenses
monthly_expenses = monthly_rent + monthly_food_budget + monthly_entertainment_budget + monthly_unforeseen_expenses
print("Monthly expenses: " + str(round(monthly_expenses, 2)))

# Finally, calculate your monthly take-home savings
monthly_savings = monthly_takehome_salary - monthly_expenses
print("Monthly savings: " + str(round(monthly_savings, 2)))

#Monthly expenses: 2550
#Monthly savings: 2408.33

# 3. FORECAST SALARY GROWTH + COST OF LIVING

#Derive the equivalent monthly salary growth 
#Derive your actual salary forecast over time using the cumulative_salary_growth_forecast we defined for you.

import numpy as np

# Create monthly forecasts up to 15 years from now
forecast_months = 12*15

# Set your annual salary growth rate
annual_salary_growth = 0.05

# Calculate your equivalent monthly salary growth rate
monthly_salary_growth = (1+annual_salary_growth)**(1/12) - 1

# Forecast the cumulative growth of your salary
cumulative_salary_growth_forecast = np.cumprod(np.repeat(1 + monthly_salary_growth, forecast_months))

# Calculate the actual salary forecast
salary_forecast = monthly_takehome_salary*cumulative_salary_growth_forecast

# Plot the forecasted salary
plt.plot(salary_forecast, color='blue')
plt.show()

# 4. FORECAST EXPENSES DUE TO INFLATION

#Set the annual inflation rate to 2.5%.
#Derive the equivalent monthly inflation rate.
#Forecast cumulative inflation growth over time.
#Derive your monthly expenses by adjusting for growth due to inflation.

import numpy as np

# Set the annual inflation rate
annual_inflation = 0.025

# Calculate the equivalent monthly inflation rate
monthly_inflation = (1+annual_inflation)**(1/12) - 1

# Forecast cumulative inflation over time
cumulative_inflation_forecast = np.cumprod(np.repeat(1 + monthly_inflation, forecast_months))

# Calculate your forecasted expenses
expenses_forecast = monthly_expenses*cumulative_inflation_forecast

# Plot the forecasted expenses
plt.plot(expenses_forecast, color='red')
plt.show()

## NET WORTH AND VALUATION

# Net Worth = Assets - Liabilities = Equity

# EXERCISE - Calculate your net worth

#Forecast your monthly savings using projections for expenses and your monthly salary.
#Calculate your cumulative savings over time.
#Print the amount you have in your savings account after 15 years of diligent savings.

import numpy as np

# Calculate your savings for each month
savings_forecast = salary_forecast - expenses_forecast

# Calculate your cumulative savings over time
cumulative_savings = np.cumsum(savings_forecast)

# Print the final cumulative savings after 15 years
final_net_worth = cumulative_savings[-1]
print("Your final net worth: " + str(round(final_net_worth, 2)))

# Plot the forecasted savings
plt.plot(cumulative_savings, color='blue')
plt.show()

#Set the investment_rate_annual to 7% and derive the monthly investment rate.
#Calculate the required monthly investment to amass $1,000,000 over 15 years.



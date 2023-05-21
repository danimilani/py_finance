## TIME VALUE OF MONEY

## GROWTH AND RATE OF RETURN

# Calculate the future value of the investment and print it out
future_value = (100 * ((1+0.06)**30))
print("Future Value of Investment: " + str(round(future_value, 2)))

##Future Value of Investment: 574.35

# COMPOUND INTEREST

# Calculate the value of a $100 investment which grows at a rate 
# of 6% per year for 30 years in a row compounded once per year and assign it to investment_1.

# Predefined variables
initial_investment = 100
growth_periods = 30
growth_rate = 0.06

# Calculate the value for the investment compounded once per year
compound_periods_1 = 1
investment_1 = initial_investment*(1 + growth_rate / compound_periods_1)**(compound_periods_1*growth_periods)
print("Investment 1: " + str(round(investment_1, 2)))
# Investment 1: 574.35

# Calculate the value of the same investment, 
# but compounded quarterly and assign it to investment_2.

# Calculate the value for the investment compounded quarterly
compound_periods_2 = 4
investment_2 = initial_investment*(1 + growth_rate / compound_periods_2)**(compound_periods_2*growth_periods)
print("Investment 2: " + str(round(investment_2, 2)))

# Calculate the value of the same investment, 
# but compounded monthly and assign it to investment_3.

# Calculate the value for the investment compounded monthly
compound_periods_3 = 12
investment_3 = initial_investment*(1 + growth_rate / compound_periods_3)**(compound_periods_3*growth_periods)
print("Investment 3: " + str(round(investment_3, 2)))

# DISCOUNT FACTORS AND DEPRECIATION

# Calculate the future value of a $100 investment that depreciates 
# in value by 5% per year for 10 years and assign it to future_value.

# Calculate the future value
initial_investment = 100
growth_rate = -0.05
growth_periods = 10
future_value = initial_investment*((1+growth_rate)**growth_periods)
print("Future value: " + str(round(future_value, 2)))

#<script.py> output:Future value: 59.87

# Calculate the discount factor of the investment and assign it to discount_factor.

# Calculate the discount factor
discount_factor = 1/((1+growth_rate)**growth_periods)
print("Discount factor: " + str(round(discount_factor, 2)))

# <script.py> output:Discount factor: 1.67

# Derive the initial value of the investment using the future value and
# the discount factor and assign it to initial_investment_again.

# Derive the initial value of the investment
initial_investment_again = future_value*discount_factor
print("Initial value: " + str(round(initial_investment_again, 2)))

# <script.py> output:Initial value: 100.0

## PRESENT AND FUTURE VALUE

# CALCULATING PV WITH NUMPY

# Calculate the present value of $100 received 3 years from now at a 1.0% inflation rate
import numpy as np
np.pv(rate=0.01, nper=3, pmt=0, fv=100)
#result:-97.05
# You have to spend 97.05 dollars in these investment conditions in order to receive a 
# future positive value of $100 after 3 years.

# CALCULATING FV WITH NUMPY

# Calculate the future value of $100 invested for 3 years at a 5% avg annual rate of return
import numpy as np
np.fv(rate=0.05, nper=3, pmt=0, pv=-100)
#result=115.76

# EXERCISE - PV

# Import numpy as np
import numpy as np

# Calculate investment_1
investment_1 = np.pv(rate=0.03, nper=15, pmt=0, fv=10000)

# Note that the present value returned is negative, so we multiply the result by -1
print("Investment 1 is worth " + str(round(-investment_1, 2)) + " in today's dollars")

# Calculate investment_2
investment_2 = np.pv(rate=0.05, nper=10, pmt=0, fv=10000)
print("Investment 2 is worth " + str(round(-investment_2, 2)) + " in today's dollars")

## <script.py> output:    Investment 1 is worth 6418.62 in today's dollars
    # Investment 2 is worth 6139.13 in today's dollars
  
# EXERCISE - FV

import numpy as np

# Calculate investment_1
investment_1 = np.fv(rate=0.05, nper=15, pmt=0, pv=-10000)
print("Investment 1 will yield a total of $" + str(round(investment_1, 2)) + " in 15 years")

# Calculate investment_2
investment_2 = np.fv(rate=0.08, nper=15, pmt=0, pv=-10000)
print("Investment 2 will yield a total of $" + str(round(investment_2, 2)) + " in 15 years")

# <script.py> output:    Investment 1 will yield a total of $20789.28 in 15 years
   # Investment 2 will yield a total of $31721.69 in 15 years

# EXERCISE - Adjusting future values for inflation

# First, forecast the FV of an investment given a rate of return
# Second, discount the FV of the investment by a projected inflation rate

import numpy as np

# Calculate investment_1
investment_1 = np.fv(rate=0.08, nper=10, pmt=0, pv=-10000)
print("Investment 1 will yield a total of $" + str(round(investment_1, 2)) + " in 10 years")

# Calculate investment_2
investment_1_discounted = np.pv(rate=0.03, nper=10, pmt=0, fv=investment_1)
print("After adjusting for inflation, investment 1 is worth $" + str(round(-investment_1_discounted, 2)) + " in today's dollars")

# <script.py> output:
   # Investment 1 will yield a total of $21589.25 in 10 years
   # After adjusting for inflation, investment 1 is worth $16064.43 in today's dollars

# NET PRESENT VALUE AND CASH FLOWS

# EXERCISE - Discounting Cash Flows

#Calculate the net present value of the investment with cash_flows at a discount rate of 3% per year, and assign it to investment_1.
#Repeat the process with a discount rate of 5% per year, and assign it to investment_2.
#Repeat the process with a discount rate of 7% per year, and assign it to investment_3.

import numpy as np

# Predefined array of cash flows
cash_flows = np.array([100, 100, 100, 100, 100])

# Calculate investment_1
investment_1 = np.npv(rate=0.03, values=cash_flows)
print("Investment 1's net present value is $" + str(round(investment_1, 2)) + " in today's dollars")

# Calculate investment_2
investment_2 = np.npv(rate=0.05, values=cash_flows)
print("Investment 2's net present value is $" + str(round(investment_2, 2)) + " in today's dollars")

# Calculate investment_3
investment_3 = np.npv(rate=0.07, values=cash_flows)
print("Investment 3's net present value is $" + str(round(investment_3, 2)) + " in today's dollars")

#<script.py> output:
    #Investment 1's net present value is $471.71 in today's dollars
    #Investment 2's net present value is $454.6 in today's dollars
    #Investment 3's net present value is $438.72 in today's dollars

# EXERCISE - Initial Project Costs

#Create a numpy array of the cash flow values for project 1, assigning it to cash_flows_1, and then do the same for project 2, assigning the values to cash_flows_2.
#Calculate the net present value of both projects 1 and 2 assuming a 3% inflation rate.

import numpy as np

# Create an array of cash flows for project 1
cash_flows_1 = np.array([-250,100,200,300,400])

# Create an array of cash flows for project 2
cash_flows_2 = np.array([-250,300,-250,300,300])

# Calculate the net present value of project 1
investment_1 = np.npv(rate=0.03, values=cash_flows_1)
print("The net present value of Investment 1 is worth $" + str(round(investment_1, 2)) + " in today's dollars")

# Calculate the net present value of project 2
investment_2 = np.npv(rate=0.03, values=cash_flows_2)
print("The net present value of Investment 2 is worth $" + str(round(investment_2, 2)) + " in today's dollars")

#<script.py> output:
    #The net present value of Investment 1 is worth $665.54 in today's dollars
    #The net present value of Investment 2 is worth $346.7 in today's dollars

# EXERCISE - Diminishing cash flows

#Calculate the present value of a single $100 payment received 30 years from now with an annual inflation rate of 3%, and assign it to investment_1.
#Calculate the present value of the same payment, but if it was received 50 and 100 years from now, and assign it to investment_2 and investment_3 respectively.

import numpy as np

# Calculate investment_1
investment_1 = np.pv(rate=0.03, nper=30, pmt=0, fv=100)
print("Investment 1 is worth $" + str(round(-investment_1, 2)) + " in today's dollars")

# Calculate investment_2
investment_2 = np.pv(rate=0.03, nper=50, pmt=0, fv=100)
print("Investment 2 is worth $" + str(round(-investment_2, 2)) + " in today's dollars")

# Calculate investment_3
investment_3 = np.pv(rate=0.03, nper=100, pmt=0, fv=100)
print("Investment 3 is worth $" + str(round(-investment_3, 2)) + " in today's dollars")

#<script.py> output:
   # Investment 1 is worth $41.2 in today's dollars
   # Investment 2 is worth $22.81 in today's dollars
   # Investment 3 is worth $5.2 in today's dollars

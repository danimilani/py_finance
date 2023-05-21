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


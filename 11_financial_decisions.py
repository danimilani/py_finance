## FINANCIAL DECISIONS

## NPV - Net Present Value
## IRR - Internal Rate of Return
## EAA - Equivalent Annual Annuity

## IRR IN NUMPY

import numpy as np
project_1 = np.array([-100,150,200])
np.irr(project_1)
#result:1.35 - Project has an IRR of 135%

# EXERCISE - Project Proposals and Cash FLows Projections

#Create a variable cf_project_1 and set it equal to a numpy array of the projected cash flows (as shown in the table) for Project 1.
#Repeat the process for Project 2 and set it equal to cf_project_2.
#Scale the original values by 1000x, i.e. multiply the original arrays by 1000.

import numpy as np

# Create a numpy array of cash flows for Project 1
cf_project_1 = np.array([-1000,200,250,300,350,400,450,500,550,600])

# Create a numpy array of cash flows for Project 2
cf_project_2 = np.array([-1000,150,225,300,375,425,500,575,600,625])

# Scale the original objects by 1000x
cf_project1 = cf_project_1*1000
cf_project2 = cf_project_2*1000

# Compare IRRs

#Set the internal rate of return for Project 1 equal to irr_project1.
#Set the internal rate of return for Project 2 equal to irr_project2.

import numpy as np

# Calculate the internal rate of return for Project 1
irr_project1 = np.irr(cf_project1)
print("Project 1 IRR: " + str(round(100*irr_project1, 2)) + "%")

# Calculate the internal rate of return for Project 2
irr_project2 = np.irr(cf_project2)
print("Project 2 IRR: " + str(round(100*irr_project2, 2)) + "%")

#<script.py> output:
    #Project 1 IRR: 28.92%
   # Project 2 IRR: 28.78%

## WACC - Weighted Average Cost of Capital

percent_equity = 0.80
percent_debt = 0.20
cost_equity = 0.14
cost_debt = 0.12
tax_rate=0.35

wacc = (percent_equity*cost_equity) + (percent_debt*cost_debt) * (1-tax_rate)
print(wacc)
#result:0.1276

# DISCOUNTING USING WACC

# Calculate the NPV of a project that produces 100$ in cash flow every year for 5 years.
# Assume a WACC of 13%

cf_project1 = np.repeat(100,5) #construct repeating array of cash flows
npv_project1 = np.npv(0.13, cf_project1) #pass array of cash flows + wacc as discount rate
print(npv_project1)
#result:397.45

# EXERCISE - DEBT AND EQUITY FINANCING

# For this exercise, assume you take out a $1,000,000 loan to finance the project,
# which will be your company's only outstanding debt. This loan will represent 50% 
# of your company's total financing of $2,000,000. The remaining funding comes from
# the market value of equity.

# Set the market value of debt
mval_debt = 1000000

# Set the market value of equity
mval_equity = 1000000

# Compute the total market value of your company's financing
mval_total = mval_debt + mval_equity

# Compute the proportion of your company's financing via debt
percent_debt = mval_debt/mval_total 
print("Debt Financing: " + str(round(100*percent_debt, 2)) + "%")

# Compute the proportion of your company's financing via equity
percent_equity = mval_equity/mval_total
print("Equity Financing: " + str(round(100*percent_equity, 2)) + "%")

#<script.py> output:
    #Debt Financing: 50.0%
    #Equity Financing: 50.0%

# CALCULATING WACC

# The proportion of debt vs equity financing is predefined
percent_debt = 0.50
percent_equity = 0.50

# Set the cost of equity
cost_equity = 0.18

# Set the cost of debt
cost_debt = 0.12

# Set the corporate tax rate
tax_rate = 0.35

# Calculate the WACC
wacc = (percent_equity*cost_equity) + (percent_debt*cost_debt) * (1 - tax_rate)
print("WACC: " + str(round(100*wacc, 2)) + "%")

#<script.py> output: WACC: 12.9%







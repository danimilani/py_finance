# Control Flow and Logic in Python

# COMPARISON OPERATORS

# Equality vs assignment

13 == 13
# result: true

count = 13
print(count)
# result: 13

# Dictionaries are equal if they have the same keys and values

d1 = {'high':56.88, 'low':33.22, 'closing':56.88}
d2 = {'high':56.88, 'low':33.22, 'closing':56.88}
print(d1 == d2)
# result: true

d1 = {'high':56.88, 'low':33.22, 'closing':56.88}
d2 = {'high':56.88, 'low':33.22, 'closing':12.89}
print(d1 == d2)
# result: false

# Not Equal Operator

print(3 != 4)
# result: True

print(3 != 3)
# result: False

# Order Operators - less than, less than or equal, more than, more than or equal

print(3 < 4) #result: True
print(1 <= 4) #result: True
print(4 > 3) #result: True
print(4 >= 1) #result: True

###########################################

# EXERCISES #

# Assignment and equality

# Assign a value to cash.
cash = 19.11

# Check if cash is equal to non-cash
print(cash == non_cash)

# Assign the value of cash to be equal non-cash
cash = non_cash

# Check if cash is equal to non-cash
print(cash == non_cash)
<script.py> output:
    False
    True

# Comparing dividends

# Check dividend is greater than zero
print(d2 > 0)

# Is dividend 1 is greater than dividend 2?
print(d1 > d2)
<script.py> output:
    True
    False

# Check dividend 1 is at least 100
print(d1 >= 100)

# Check dividend 2 is at least as much dividend 1
print(d1 <= d2)
<script.py> output:
    True
    True

###########################################

# Boolean Operators

# Operations done between true or false operators, logical conjunction, disjunction and negation

# Evaluates as False in Python
# Constants: false and none
# Numeric zero: 0 and 0.0
# Length of zero: "", [] and {}

# Evaluates as True in Python
# Almost everything else

# AND Operator
True and True 
# Result: true

# OR Operator
True or True 
# Result: true

# SHORT CIRCUIT Operation
# If the first method returns false, the second will not be called.

is_current() and is_investment()
# result: false

is_current() or is_investment()
# result: true

# NOT Operator - it returns the boolean opposite of an item directly following it
not True 
# Result: False

not True == False
# result: True



###########################################

# EXERCISES #

## Decisions with Boolean operations

# Print the given variables
print(is_investment_account)
print(balance_positive)

# Decide if this account is cantidate for trading advice
potential_trade = is_investment_account and balance_positive

# Print if this represents a potential trade
print(potential_trade)
<script.py> output:
    True
    True
    True

## Assigning variables with Boolean operators

# Assign a default action if no input
action = input_action or "Hold"

# Print the action
print(action)

# Assign action only if trades can be made
do_action = is_trading_day and action

# Print the action to do
print(do_action)
<script.py> output:
    Hold
    False

## Negating with Boolean operators

print(closing_prices)

# Assigning True if we need to get the prices
not_prices = not closing_prices

print(not_prices)

# Get prices if market is closed and we don't have prices
get_prices = not (market_closed and not_prices)

print(get_prices)
<script.py> output:
    []
    True
    True

###########################################

# IF STATEMENTS - Compound statements, the value controls the executions of the statements

if<expression>:
  statement

if<expression>:  statement; statement; statement

if x < y:
if x in y:
if x and y:
if x:

trns = {'symbol':'TSLA', 'type':'BUY', 'amount':300}

if trns['type'] == 'SELL':
  print(trns['amount'])

trns['type'] == 'SELL'
# Return: false

trns = {'symbol':'TSLA', 'type':'SELL', 'amount':200}

if trns['type'] == 'SELL':
  print(trns['amount'])

trns['type'] == 'SELL'
# Return: 200

# ELSE and ELIF

if x in y:
  print("I found x in y")
else:
  print("No x in y")

if x == y:
  print("equals")
elif x < y:
  print("less")
elif x > y:
  print("more")
elif x == 0
  print("zero")
else:
  print("None of the above")

###########################################

# EXERCISES #

## Comparing sales and purchases

# Get number of purchases
num_purchases = len(purchases)
# Get number of sales
num_sales = len(sales)

# Check if more sales than purchases
if num_purchases < num_sales:
    print('buy more')

# Check if fewer sales than purchases
if num_sales < num_purchases:
    print('sell more')

# Check if both lists are empty
if not (purchases or sales):
    print('No sales or purchases')


## Branching with elif and else

# Get the symbol value
symbol = trn['symbol']

# Check if Apple stock
if symbol == 'APPL':
    appl.append(trn)

# Get the symbol value
symbol = trn['symbol']

# Check if Apple stock
if symbol == 'APPL':
    appl.append(trn)
# Check if Tesla stock
elif symbol == 'TSLA':
    tsla.append(trn)
# Check if Amazon stock
elif symbol == 'AMZN':
    amzn.append(trn)
# Handle other companies
else:
    print(symbol)

###########################################

# FOR AND WHILE LOOPS

# FOR Loop - Loops through the items in the sequence

for <variable> in <sequence>:

# LIST EXAMPLE
for x in [0,1,2]:
  print(x)

# result:
0
1
2

# DICTIONARY EXAMPLE
symbols = {'037833100':'AAPL',
           '17275R102':'CSCO',
           '68389X105':'ORCL'}

for k in symbols:
  print(symbols[k])

# result:
AAPL
CSCO
ORCL

# STRING EXAMPLE

for x in "ORACLE":
  print(x)

# result:
O
R
A
C
L
E

# WHILE Loop - execute the code as long as the expression is true

while<expression>:

# EXAMPLE

x = 0
while x < 5:
  print(x)
  x = (x + 1)

# result:
0
1
2
3
4

# INFINITE LOOPS

# Skipping with continue

for x in [0,1,2,3]:
  if x == 2:
    continue
  print(x)

# result:
0
1
3

# Stopping with break

while True:
  transaction = get_transaction()
  if transaction ['symbol'] == 'ORCL':
    print('The current symbol is ORCL, break now')
    break
  print('Not ORCL')

# result:
Not ORCL
Not ORCL
Not ORCL
The current symbol is ORCL, break now

###########################################

# EXERCISES #

## Breaking out of a for loop

# Loop through buys
for buy in buys:
    print('Buying ' + buy['symbol'])
    new_balance = balance - buy['total_cost']
    balance = new_balance

print(balance)
<script.py> output:
    Buying AAPL
    Buying ORCL
    Buying CSCO
    -101

for buy in buys:
    print('Buying ' + buy['symbol'])
    new_balance = balance - buy['total_cost']
    if new_balance < 0:
        print('Unable to finish buys')
        break
    balance = new_balance

print(balance)
<script.py> output:
    Buying AAPL
    Buying ORCL
    Buying CSCO
    Unable to finish buys
    99

## Controlling loop execution

# Loop while true
while True:
    net_exports = nea.get(query_date, -1)
    query_date = datetime(query_date.year - 1, 1, 1)
    # Skip if net exports are not positive
    if net_exports < 0:
        continue   
    surplus_years.append(query_date)
    # Check if 5 years have been collected
    if len(surplus_years) == 5:
        # Stop the loop
        break
print(surplus_years)
<script.py> output:
    [datetime.datetime(1974, 1, 1, 0, 0), datetime.datetime(1972, 1, 1, 0, 0), datetime.datetime(1970, 1, 1, 0, 0), datetime.datetime(1969, 1, 1, 0, 0), datetime.datetime(1968, 1, 1, 0, 0)]


###########################################

# Get loan details.

money_owed = float(input("How much money do you owe, in dollars?\n"))
apr = float(input("What is the APR?\n"))
payment = float(input("What will your monthly payment be, in dollars? \n"))
months = int(input("How many months do you want to see results for? \n"))

monthly_rate = apr/100/12

interest_paid = money_owed * monthly_rate
money_owed
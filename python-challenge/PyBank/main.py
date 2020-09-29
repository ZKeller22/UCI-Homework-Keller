# Import libraries

import os
import csv

# Create Rquired Variables
profit = []
monthly_changes = []
date = []

total = 0
count = 0
total_change = 0
initial_profit = 0
# Path to collect data from the Resources folder
budget_csv = os.path.join("..","Resources","budget_data.csv")


# Read in the csv file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header= next(csvreader)
    # Run through each row in the file
    for row in csvreader:
        count = count +1
        date.append(row[0])
        profit.append(row[1])
        total = total + int(row[1])
        last_profit = int(row[1])
        monthly_profit_change = last_profit- initial_profit
        monthly_changes.append(monthly_profit_change)
        total_change = total_change + monthly_profit_change
        initial_profit = last_profit
        average_change = (total_change/count)
        greatest_increase_profits = max(monthly_changes)
        greatest_decrease_profits = min(monthly_changes)
        date_increase = date[monthly_changes.index(greatest_increase_profits)]
        date_decrease = date[monthly_changes.index(greatest_decrease_profits)]

print (total)        
print(count)
print(average_change)
print(greatest_increase_profits)
print(greatest_decrease_profits)
print(date_increase)   
print(date_decrease)     

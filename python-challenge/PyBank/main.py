# Import modules

import os
import csv

# Create empty lists to store profit, month changes, and date
profit = []
monthly_changes = []
date = []

#Create variables to calculate number of months, total profit, change in profit and initla profit
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

        # Calculate the total months
        count = count +1
        #Add each date row to date list
        date.append(row[0])
        #add each profit row to profit list
        profit.append(row[1])
        #Calculate the total profit
        total = total + int(row[1])

        #Calculate what the monthly changes in profit will be and store the value in the monthly_changes list
        last_profit = int(row[1])
        monthly_profit_change = last_profit- initial_profit
        monthly_changes.append(monthly_profit_change)

        total_change = total_change + monthly_profit_change
        initial_profit = last_profit

        
        
        

        #Calculate the greatest increase and decreae in profit and the corresponding date
        greatest_increase_profits = max(monthly_changes)
        greatest_decrease_profits = min(monthly_changes)

        
        date_increase = date[monthly_changes.index(greatest_increase_profits)]
        date_decrease = date[monthly_changes.index(greatest_decrease_profits)]
    
    #Calculate the average change in profit
    monthly_changes.pop(0)


    avg= sum(monthly_changes)/ len(monthly_changes)
    

#Print out the results
print("Fiancial Analysis")
print("-------------------------------------------------------")
print (f"Total Months: {count}")

print(f"Total Profit: ${total}")

print(f"Average Change: ${round(avg,2)}")

print(f"Greatest Increase in Profit:  {date_increase} (${greatest_increase_profits})")

print(f"Greatest Decrease in Profit:  {date_decrease} (${greatest_decrease_profits})")



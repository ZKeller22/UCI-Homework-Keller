# Import libraries

import os
import csv


# Path to collect data from the Resources folder
budget_csv = os.path.join("..", "Resources","budget_data.csv")

# Define the function and have it accept the 'budgetData' as its sole parameter



# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header= next(csvreader)
    data= list(csvreader)
    row_count= len(data)
    print(f"Total Months: {row_count}")

    total = sum(int(row[1]) for row in csvreader
    print(total)


# Import modules

import os
import csv

#Define Lists and variables

total_vote = 0
candidate_list = []




# Path to collect data from the Resources folder
election_csv = os.path.join("..","Resources","election_data.csv")


# Read in the csv file
with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header= next(csvreader)

    for row in csvreader:
        #Get the total votes
        total_vote += 1

print("ELECTION RESULTS")
print("------------------------")
print(f"Total Votes: {total_vote}")
print("------------------------")
    
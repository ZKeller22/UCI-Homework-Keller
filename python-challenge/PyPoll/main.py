# Import modules

import os
import csv

#Define Lists and variables
total_vote = 0
candidates = []
candidate_unique = []
vote_count = []
vote_pecent = []

# Path to collect data from the Resources folder
election_csv = os.path.join("..","Resources","election_data.csv")


# Read in the csv file
with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header= next(csvreader,None)

    for header in csvreader:
        #Get the total votes
        total_vote += 1
        candidate = header[2]
        #Add candidates to the candidate list

        # add votes to candidate running total. HA a pun.
        if candidate in candidates:
            candidate_unique = candidates.index(candidates)
            vote_count[candidate_unique] = vote_count[candidate_unique] + 1

        # Make new spot for candidate in list
        else:
            candidates.append(candidate)
            vote_count.append(1)
    #Declare the other variables:
    percentages = []
    max_votes = vote_count[0]
    max_index = 0
    #Work out percentages and winner (in a For Loop)
    for count in range(len(candidates)):
        vote_percentage = vote_count[count]/total_vote*100
        percentages.append(vote_percentage)
        if vote_count[count] > max_votes:
            max_votes = vote_count[count]
            print(max_votes)
            max_index = count
    winner = candidates[max_index]
   
    percentages = [round(i,2) for i in percentages]

print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_vote}")
print("--------------------------")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_count[count]})")
print("--------------------------")
print(f"Winner:  {winner}")
print("--------------------------")



    
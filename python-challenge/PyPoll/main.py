# Import modules

import os
import csv

#Define ists and variables
total_vote = 0
candidate_list = []
vote_count = []
vote_pecent = []

# Path to collect data from the Resources folder

election_csv = os.path.join("..","Resources","election_data.csv")


# Read in the csv file
with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header= next(csvreader,None)

    for row in csvreader:
        #Get the total votes
        total_vote += 1
        candidate = row[2]

        # Add votes to candidate running total
        if candidate in candidate_list:
            candidate_unique = candidate_list.index(candidate)
            vote_count[candidate_unique] = vote_count[candidate_unique] + 1

        # Make new spot for candidate in list
        else:
            candidate_list.append(candidate)
            vote_count.append(1)
    #Declare the additional variables:
    percentages = []
    max_votes = vote_count[0]
    max_index = 0

    #Calcualte who won and the percentage and total vote per candidate
    for count in range(len(candidate_list)):
        vote_percentage = vote_count[count]/total_vote*100
        percentages.append(vote_percentage)
        if vote_count[count] > max_votes:
            max_votes = vote_count[count]
            print(max_votes)
            max_index = count
    winner = candidate_list[max_index]
    #Calculate the percentages for each candidate and round number
    percentages = [round(i,2) for i in percentages]

#Print out the results to the terminal
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_vote}")
print("--------------------------")
for count in range(len(candidate_list)):
    print(f"{candidate_list[count]}: {percentages[count]}% ({vote_count[count]})")
print("--------------------------")
print(f"Winner:  {winner}")
print("--------------------------")

#  Write output to the text file

with open("vote_analysis.txt", "w") as text:

    text.write("Election Results" + "\n")

    text.write("--------------------------------\n")

    text.write(f"Total Votes: {total_vote}" +"\n")

    for count in range(len(candidate_list)):
        text.write(f"{candidate_list[count]}: {percentages[count]}% ({vote_count[count]})"+ "\n")

    text.write("--------------------------------\n")

    text.write(f"Winner:  {winner}"+"\n")

    text.write("--------------------------------\n")



    
#starting off initializing and reading in the CSV file using code from activity 3-8
#initialize
import os
import csv

#set file path
csvpath = 'C:/Users/Eric/Downloads/python-challenge/PyPoll/resources/election_data.csv'

#open file
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    #running total number of votes cast
    vote_total = 0
    #list of canidates
    canidates = []
    #dictionary to count votes per canidate
    canidate_votes = {}
    for row in csvreader:
        #increase count of total votes
        vote_total += 1
        #add to list of canidates if not already in list
        if row[2] not in canidates:
            canidates.append(row[2])
            #add new canidate to canidate vote dictionary
            canidate_votes[row[2]]=0

        #increment vote count if canidate is already in list
        canidate_votes[row[2]] +=1 

#export results
output_path = 'C:/Users/Eric/Downloads/python-challenge/PyPoll/analysis/output.txt'

with open(output_path, 'w') as f:
    f.write('Election Results\n--------------\n')
    print('Election Results\n--------------\n')
    f.write('Total Votes: ' + str(vote_total) + '\n--------------\n')
    print('Total Votes: ' + str(vote_total) + '\n--------------\n')

    #2 variables to store winning canidate and the number of their votes
    highvotes = 0
    winner = ""

    for canidate in canidate_votes:
        #get number of votes from dictionary and calculate percentage votes
        votes=canidate_votes[canidate]
        percentage_votes = votes/vote_total*100
        f.write(canidate + ": " + str(percentage_votes) + "% (" + str(votes) + ")\n")
        print(canidate + ": " + str(percentage_votes) + "% (" + str(votes) + ")\n")

        #determine if canidate has highest number of votes
        if votes > highvotes:
            highvotes = votes
            winner = canidate

    f.write('--------------\nWinner: ' + str(winner) + '\n--------------')
    print('--------------\nWinner: ' + str(winner) + '\n--------------')
#Unit 3 Homework

#PyPoll Challenge

#import os and csv
import os
import csv

#Defining variables
candidates = []
total_votes = 0
votes = {}
candidate_name = []
total_votes = 0

#Declaring file path
csvpath = os.path.join("Resources","election_data.csv")

#Opening CSV file and skipping the header line
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        
        #Counting total number of votes
        total_votes += 1

        #Identifying where the candidate name is located
        candidate_name = row[2]

        #Adds candidate names to our list of candidates if not already included and counts their votes
        if row[2] not in candidates:
            candidates.append(candidate_name)
            votes[candidate_name] = 0
        votes[candidate_name] += 1
    candidates.append(votes)

#Print Election Results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

#Calculating each candidates share of the vote and printing the results of each candidate
for candidate_name in votes:
    print(f"{candidate_name}:  {str(round(votes[candidate_name]/total_votes*100,3))}% ({votes[candidate_name]})")
print("-------------------------")

#Calculate the winner of the vote and printing
winner = max(votes, key=votes.get)
print(f'Winner: {winner}')
print("-------------------------")

#Creating text file with the same output
Analysis_File = os.path.join("Analysis", "Analysis_File.txt")
with open(Analysis_File,"w") as Analysis_Output:
    Analysis_Output.write(f"Election Results\n")
    Analysis_Output.write(f"-------------------------\n")
    Analysis_Output.write(f"Total Votes: {total_votes}\n")
    Analysis_Output.write(f"-------------------------\n")
    for candidate_name in votes:
        Analysis_Output.write(f"{candidate_name}:  {str(round(votes[candidate_name]/total_votes*100,3))}% ({votes[candidate_name]})\n")
    Analysis_Output.write(f"-------------------------\n")
    Analysis_Output.write(f"Winner: {winner}\n")    
    Analysis_Output.write(f"-------------------------\n")
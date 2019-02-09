# Import Module used in the program
import os
import operator
import csv
# Provide file location
csvpath = os.path.join('..', 'Resources', 'election_data.csv')
# Improved Reading using CSV module
with open(csvpath, newline='') as csvfile:
# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
# Read the header row first 
    csv_header = next(csvreader)
# Sort the csv file by canditate name    
    csvsorted = sorted(csvreader,key=operator.itemgetter(2))
# Lists to store data
    candidateName = []
    candidateVote = []
    currentCandidate = ""
    vote = 0
# Count the total of rows which is also total of votes  
    votecount = sum(1 for line in csvsorted)   
# Assign first row value to the store data
    currentCandidate = csvsorted[0][2]
    candidateName.append(csvsorted[0][2])
#Read the csv file and count votes and save candidate name
    for row in csvsorted:       
        if currentCandidate == row[2]:
            vote += 1
        else:
            currentCandidate = row[2]
            candidateName.append(row[2])
            candidateVote.append(vote)
            vote = 0
    candidateVote.append(vote)
#Function to calculate percentage of Votes            
    def percCal(totalVote):
        return (totalVote/votecount) * 100
#With Dictionary, we will find the Winner
    DictCandidateVote = dict(zip(candidateName,candidateVote))
    winner = max(DictCandidateVote, key=DictCandidateVote.get)
    print("Election Rasults")
    print("------------------------------")
    print(f"Total Votes: {votecount}")
    print("------------------------------")
    for c,v in zip(candidateName,candidateVote): 
        print(f"{c}: {percCal(v):.3f}% ({v})")
    print("------------------------------")
    print(f"Winnner: {winner}")
    print("------------------------------")
#Section to write into file
    csvpath = os.path.join('..', 'Resources', 'electionResult.txt')
    with open(csvpath, "w") as txtfile:
#Write data in the Text file
       txtfile.write(f"Election Results")
       txtfile.write("\n")
       txtfile.write(f"----------------------------")
       txtfile.write("\n")
       txtfile.write(f"Total Votes: {votecount}")
       txtfile.write("\n")
       txtfile.write(f"----------------------------")
       txtfile.write("\n")
       for c,v in zip(candidateName,candidateVote): 
           txtfile.write(f"{c}: {percCal(v):.3f}% ({v})")
           txtfile.write("\n")
       txtfile.write(f"----------------------------")
       txtfile.write("\n")
       txtfile.write(f"Winnner: {winner}")
       txtfile.write("\n")
       txtfile.write(f"----------------------------")
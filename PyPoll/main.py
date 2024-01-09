import os
import csv

csvpath = os.path.join('Resources/election_data.csv')

votes = 0

candidates = []
candidate_names = []
count = []
percent = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csvheader = next(csvfile)

    for row in csvreader:
        votes = votes + 1
        candidates.append(row[2])
    
    for i in set(candidates):
        candidate_names.append(i)
        votes_won = candidates.count(i)
        count.append(votes_won)
        percent_votes_won = (votes_won/votes)*100
        percent.append(percent_votes_won)

    winning_count = max(count)
    winner = candidate_names[count.index(winning_count)]


print("Election Results")
print("-------------------------")
print("Total Votes: " + str(votes))
print("-------------------------")
for i in range(len(candidate_names)):
    print(candidate_names[i] + ": " + str(percent[i]) + "% (" + str(count[i]) + ")")
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

outFileName="../analysis/results.txt"
outFile=open(outFileName, "w")
outFile.write("Election Results \n")
outFile.write("---------------------------- \n")
outFile.write("Total Votes: " + str(votes) + "\n") 
outFile.write("---------------------------- \n")
for i in range(len(candidate_names)):
    outFile.write(candidate_names[i] + ": " + str(percent[i]) + "% (" + str(count[i]) + ") \n")
outFile.write("---------------------------- \n")
outFile.write("Winner: " + winner + "\n")
outFile.write("---------------------------- \n")
outFile.close

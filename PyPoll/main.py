# PyPoll 
# import modules 
import os
import csv

# file path 
election_data_csv=os.path.join("Resources", "election_data.csv")

# output text file path
import os.path
text_file="Output.txt"
txtpath=os.path.join("analysis",text_file)
f=open(txtpath,'w')

# variables 
Total_votes=0
# dictionary 
candidatevotes={}

# open csv 
with open(election_data_csv) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csvheader=next(csvreader)

 # loop
    for row in csvreader: 
        Total_votes= Total_votes + 1
        if row[2]not in candidatevotes:
            candidatevotes[row[2]]=1
        else:
            candidatevotes[row[2]] += 1

# print/write 
print(f"Election Results")
print(f"\n-------------------------")
print(f"\nTotal Votes:"+str(Total_votes))
print(f"\n-------------------------")
# Format - "Name: (Percentage of votes to third decimal) (Total number of votes)"
for candidate, votes in candidatevotes.items():
    print(candidate + ": "+" {:.3%}".format(votes/Total_votes)+" ("+str(votes)+")")
print(f"\n-------------------------")
winner=max(candidatevotes,key=candidatevotes.get)
print(f"\nWinner: {winner}")

f.write(f"Election Results")
f.write(f"\n-------------------------")
f.write(f"\nTotal Votes:"+str(Total_votes))
f.write(f"\n-------------------------\n")

# Format - "Name: (Percentage of votes to third decimal) (Total number of votes)"
for candidate, votes in candidatevotes.items():
    f.write(candidate + ":" + "{:.3%}".format(votes/Total_votes) + "(" + str(votes) + ")" "\n")
    
f.write(f"-------------------------")
winner=max(candidatevotes,key=candidatevotes.get)
f.write(f"\nWinner: {winner}")
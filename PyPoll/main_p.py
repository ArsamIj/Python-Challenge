# import libraries
import os
import csv

#create paths to read/write data
csvpath = os.path.join("Resources", "election_data.csv")
output = os.path.join("Analysis", "Election_Result.txt")

#create lists to store the data from the csv file
B_ID = []
Candidate = []

#create lists and variables for data computation
TotalVotes = 0
Shortlist = []
CanVotes_1 = 0 
CanVotes_2 = 0 
CanVotes_3 = 0
VoteCount = []
PerCount = []

print("Election Results")
print("-----------------------------")

#open the file
with open(csvpath) as csvfile:

    #read the file
    csvreader = csv.reader(csvfile, delimiter = ",")

    #store and skip the header
    csv_header = next(csvreader)

    #read the data row by row and store the data in lists
    for row in csvreader:
        B_ID.append(row[0])
        Candidate.append(row[2])

        #compute the total number of votes cast
        TotalVotes = TotalVotes + 1
    
    print(f"Total Votes Cast: " + str(TotalVotes))
    print("-----------------------------")

    #create a shortlist of candidates
    for i in range(1, len(Candidate)):
        if Candidate[i] not in Shortlist:
            Shortlist.append(Candidate[i])

    #compute the number of votes cast for each candidate
    for i in range(len(Candidate)):
        if Candidate[i] == Shortlist[0]:  
            CanVotes_1 = CanVotes_1 + 1
        if Candidate[i] == Shortlist[1]:
            CanVotes_2 = CanVotes_2 + 1
        if Candidate[i] == Shortlist[2]:
            CanVotes_3 = CanVotes_3 + 1

    #append the number of votes cast per candidate into a list
    VoteCount.append(CanVotes_1)
    VoteCount.append(CanVotes_2)
    VoteCount.append(CanVotes_3)

    #compute the maximum number of votes cast for a candidate
    maxVote = max(VoteCount)

    #compute the percentage of votes cast per candidate
    PerCount.append("{:.2%}".format(CanVotes_1/TotalVotes))
    PerCount.append("{:.2%}".format(CanVotes_2/TotalVotes))
    PerCount.append("{:.2%}".format(CanVotes_3/TotalVotes))

    #print results in terminal
    for i in range(len(Shortlist)):
        print(Shortlist[i] + ": " + str(PerCount[i]) + " (" + str(VoteCount[i]) + ")")

    print("-----------------------------")

    #Comute the winner based on max vote count 
    for i in range(len(VoteCount)):
        if VoteCount[i] == maxVote:
            Winner = Shortlist[i]
    
    #print the winner
    print(f"Winner : " + Winner)
    print("-----------------------------")

#print the results in an appropriate text file
with open(output, 'w') as analysisfile:

    analysisfile.writelines("Election Results")
    analysisfile.writelines('\n')
    analysisfile.writelines("-----------------------------")
    analysisfile.writelines('\n')
    analysisfile.writelines("Total Votes Cast: " + str(TotalVotes))
    analysisfile.writelines('\n')
    analysisfile.writelines("-----------------------------")
    analysisfile.writelines('\n')
    for i in range(len(Shortlist)):
        analysisfile.writelines(Shortlist[i] + ": " + str(PerCount[i]) + " (" + str(VoteCount[i]) + ")")
        analysisfile.writelines('\n')
    analysisfile.writelines("-----------------------------")
    analysisfile.writelines('\n')
    analysisfile.writelines("Winner : " + str(Winner))
    analysisfile.writelines('\n')
    analysisfile.writelines("-----------------------------")


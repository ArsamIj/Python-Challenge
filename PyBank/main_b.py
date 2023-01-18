# import libraries
import os
import csv

#create paths to read/write data
csvpath = os.path.join("Resources", "budget_data.csv")
output = os.path.join("Analysis", "Bank_Result.txt")

#identify lists to collect the data from the csv file
Profit_Loss = []
Date = []
#identify variables and lists to be used for output
totalmonths = 0
totalprofit = 0
minDate = []
maxDate = []

#create new lists for saving data
Change=[]
Month_Change = []

print("Financial Analysis")
print("-----------------------------")

#open resource
with open(csvpath) as csvfile:
    #read data from resource
    csvreader = csv.reader(csvfile, delimiter = ",")

    #read and skip header
    csv_header = next(csvreader)

    #read each row at a times
    for row in csvreader:

        #transfering data to lists
        Date.append(row[0])
        Profit_Loss.append(row[1])

        #computing total months and total profit/loss
        totalmonths = totalmonths + 1
        totalprofit = totalprofit + int(row[1])

    print(f"Total Months: " + str(totalmonths))
    print(f"Total: " + '${}'.format(str(totalprofit)))

    #compute and append the difference in profit and loss to a list 
    #and creating a parallel list for date saving 
    for i in range(1, len(Profit_Loss)):
        Change.append(int(Profit_Loss[i]) - int(Profit_Loss[i-1]))
        Month_Change.append(Date[i])
    
    #compute the average of the differences between each month
    Average_profit = round((sum(Change)/len(Change)), 2)
    print(f"Average Change: " + '${}'.format(str(Average_profit)))

    #compute the maximum change and minimum change
    MaxChange = max(Change)
    MinChange = min(Change)
    
    #identify the date of the max and min change
    for i in range(1, len(Change)):
        if Change[i] == MaxChange:
            maxDate = Month_Change[i]
        if Change[i] == MinChange:
            minDate = Month_Change[i]

    print("Greatest Increase in Profits: " + str(maxDate) + ", " + '${}'.format(str(MaxChange)))
    print("Greatest Decrease in Profits: " + str(minDate) + ",  " + '${}'.format(str(MinChange)))

#write the data to the appropriate text file
with open(output, 'w') as analysisfile:

    analysisfile.writelines("Financial Analysis")
    analysisfile.writelines('\n')
    analysisfile.writelines("-----------------------------")
    analysisfile.writelines('\n')
    analysisfile.writelines("Total Months: " + str(totalmonths))
    analysisfile.writelines('\n')
    analysisfile.writelines("Total: " + '${}'.format(str(totalprofit)))
    analysisfile.writelines('\n')
    analysisfile.writelines("Average Change: " + '${}'.format(str(Average_profit)))
    analysisfile.writelines('\n')
    analysisfile.writelines("Greatest Increase in Profits: " + str(maxDate) + ", " + '${}'.format(str(MaxChange)))
    analysisfile.writelines('\n')
    analysisfile.writelines("Greatest Decrease in Profits: " + str(minDate) + ", " + '${}'.format(str(MinChange)))

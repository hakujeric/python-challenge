# Module to read file paths across operating systems
import os
# Module for reading CSV files
import csv
# Provide file location
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
# Improved Reading using CSV module
with open(csvpath, newline='') as csvfile:
# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
# Read the header row first 
    csv_header = next(csvreader)
# Lists to store data
    dateList = []
    amountList = []
    amountChange = []
    # Loop through csv file
    for row in csvreader:
    # Add Date
        dateList.append(row[0])
    # Add Profit/Loss Amount
        amountList.append(float(row[1]))
    #To calculate changes in Profit/Losses, we need list with all monthly change
    for i in range(len(amountList)-1):
        # Take the difference between two months and append to monthly profit change
        amountChange.append(amountList[i+1]-amountList[i])
    #With the list created List above we can get the maximum & minimum change
    maxChange = format(max(amountChange),',.2f')
    minChange = format(min(amountChange),',.2f')
    #Locate the Index to find the month of max & min change
    IndexMaxMonth = amountChange.index(max(amountChange)) + 1
    IndexMinMonth = amountChange.index(min(amountChange)) + 1
    #Section to print the result
    print("**** PyBank Financial Analysis ****")
    print("-----------------------------------")
    #The total number of months included in the dataset
    print(f"Total Months: {len(dateList)}")
    #The net total amount of "Profit/Losses" over the entire period
    print(f"Total: ${format(sum(amountList),',.2f')}")
    #The average of the changes in "Profit/Losses" over the entire period
    print(f"Average Change: ${format(round(sum(amountChange)/len(amountChange),2),',.2f')}")
    #The greatest increase in profits (date and amount) over the entire period
    print(f"The greatest increase in profits (date and amount): {dateList[IndexMaxMonth]} (${maxChange})")
    #The greatest decrease in losses (date and amount) over the entire period
    print(f"The greatest decrease in losses (date and amount): {dateList[IndexMinMonth]} (${minChange})")
    print("-----------------------------------")
    #Section to write into file
    csvpath = os.path.join('..', 'Resources', 'financialAnalysis.txt')
    with open(csvpath, "w") as txtfile:
        txtfile.write("**** PyBank Financial Analysis ****")
        txtfile.write("\n")
        txtfile.write(f"Total Months: {len(dateList)}")
        txtfile.write("\n")
        txtfile.write(f"Total: ${format(sum(amountList),',.2f')}")
        txtfile.write("\n")
        txtfile.write(f"Average Change: ${format(round(sum(amountChange)/len(amountChange),2),',.2f')}")
        txtfile.write("\n")
        txtfile.write(f"The greatest increase in profits (date and amount): {dateList[IndexMaxMonth]} (${maxChange})")
        txtfile.write("\n")
        txtfile.write(f"The greatest decrease in losses (date and amount): {dateList[IndexMinMonth]} (${minChange})")
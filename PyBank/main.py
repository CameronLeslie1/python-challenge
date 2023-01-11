# Unit 3 Homework

#PyBank Challenge

#import os and csv
import os
import csv

# Defining Lists
months = []
profit_loss_changes = []

#Defining Variables
count_months = 0
total_profit_loss = 0
previous_profit_loss = 0
current_profit_loss = 0
profit_loss_change = 0

#Declaring file path
csvpath = os.path.join("Resources","budget_data.csv")

#Module_3/python-challenge/PyBank/Resources/budget_data.csv
#Module_3/python-challenge/PyBank/main.py

#Open File and print headers
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")


    for row in csvreader:
        #Count total number of months.
        count_months +=1

        #Count total profit/loss
        current_profit_loss = int(row[1])
        total_profit_loss += current_profit_loss

        #For first month, no change in profit/loss. Sets up next calc.
        if count_months ==1:
            previous_profit_loss = current_profit_loss
        
        #For every row after the first, calculate change in profit/loss from previous month. Add to our Months list and reset previous month profit/loss for next calc.
        else:
            profit_loss_change = current_profit_loss - previous_profit_loss
            months.append(row[0])
            profit_loss_changes.append(profit_loss_change)
            previous_profit_loss = current_profit_loss

#Calculating average profit/loss, minimum, and maximum
Sum_Changes_Profit_Loss = sum(profit_loss_changes)
Mean_Profit_Loss = round(Sum_Changes_Profit_Loss/(count_months-1),2)
Max_Profit = max(profit_loss_changes)
Min_Profit = min(profit_loss_changes)

#Creating variable showing what month min/max profit/loss occured
Max_Profit_Month = profit_loss_changes.index(Max_Profit)
Min_Profit_Month = profit_loss_changes.index(Min_Profit)

#Converting what number month to the corresponding date from months list
Max_Month_Converter = months[Max_Profit_Month]
Min_Month_Converter = months[Min_Profit_Month]

#Printing output
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: ${count_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: {Mean_Profit_Loss}")
print(f"Greatest Increase in Profits: {Max_Month_Converter} (${Max_Profit})")
print(f"Greatest Decrease in Profits: {Min_Month_Converter} (${Min_Profit})")

#Creating text file with the same output
Analysis_File = os.path.join("Analysis", "Analysis_File.txt")
with open(Analysis_File,"w") as Analysis_Output:
    Analysis_Output.write(f"Financial Analysis\n")
    Analysis_Output.write(f"----------------------------\n")
    Analysis_Output.write(f"Total Months: ${count_months}\n")
    Analysis_Output.write(f"Total: ${total_profit_loss}\n")
    Analysis_Output.write(f"Average Change: {Mean_Profit_Loss}\n")    
    Analysis_Output.write(f"Greatest Increase in Profits: {Max_Month_Converter} (${Max_Profit})\n")  
    Analysis_Output.write(f"Greatest Decrease in Profits: {Min_Month_Converter} (${Min_Profit})\n")  
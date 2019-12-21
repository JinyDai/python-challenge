#First import the os module for read csv file
import os
import csv
#import the path for the budget data base

pybank_csv=os.path.join('PyBank','02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

#create a place holder to hold required data
profit=[]
monthly_change=[]
months = []
#initate the variable data
total_profit=0
pre_profit=0
total_change_profit=0


# Read in the CSV file
with open(pybank_csv,"r", newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    # skip header to count the total months
    header = next(csvreader,None)
    #start the loop to calculate
    
    for row in csvreader:
        months.append(row[0])
    # calculate total number of month (eaqul to the legth of the list without header)
        month_number=len(months)
    #append each profit/loss at profit list and calculate the total amount
        profit.append(row[1])
        total_profit=total_profit+int(row[1])
    #calcualte average change in profit/loss, the average of (next month profit/loss-previous month profit/loss)
    #skip the first month's value
        next_profit = int(row[1])
        monthly_change_profit=next_profit-pre_profit
    #reset the previous month profit/loss
        pre_profit=next_profit
    #create the list for all the profit changes
        monthly_change.append(monthly_change_profit) 
    #calculate the average change
    monthly_change[0]=0
    avg_change=round(sum(monthly_change)/(len(monthly_change)-1),2)
    print(avg_change)
    #find the greatest increase in profit
    greatest_profit=max(monthly_change)
    #find the greatest loss in profit
    greatest_loss=min(monthly_change)
    #find the date for the greatest profit and loss
    greatest_profit_date = months[monthly_change.index(greatest_profit)]
    greatest_loss_date = months[monthly_change.index(greatest_loss)]

    print("Financial Analysis")
    print("-------------------------")
    print(f"Total Months: {month_number}")
    print(f"Total Profit: ${total_profit}")
    print(f"Average Change: ${avg_change}")
    print(f"Greatest Increase in Profits: {greatest_profit_date} ${greatest_profit}")
    print(f"Greatest Decrease in Profits: {greatest_loss_date} ${greatest_loss}")

output_path=os.path.join('PyBank','pyBank_output.txt')
with open(output_path,'w') as text:
    text.write("Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write(f"Total Months: {month_number} \n")
    text.write(f"Total Profit: ${total_profit} \n")
    text.write(f"Average Change: ${avg_change} \n")
    text.write(f"Greatest Increase in Profits: {greatest_profit_date} ${greatest_profit} \n")
    text.write(f"Greatest Decrease in Profits: {greatest_loss_date} ${greatest_loss} \n")

     
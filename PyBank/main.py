import os
import csv

csvpath = os.path.join('..','Resources','budget_data.csv')

total_months = 0
total_profit_losses = 0
previous_profit_loss = 0
monthly_changes = []
dates = []

with open(csvpath, encoding='UTF-8') as csvfile:

    csvreader = csv.reader(csvfile)
    
    # Skip the header row
    next(csvreader)

    for row in csvreader:
        # Extract data from the current row
        date = row[0]
        profit_loss = int(row[1])

        # Calculate total months and total profit/losses
        total_months += 1
        total_profit_losses += profit_loss

        # Calculate and store the change in profit/losses
        if total_months > 1:
            monthly_change = profit_loss - previous_profit_loss
            monthly_changes.append(monthly_change)
            dates.append(date)

        previous_profit_loss = profit_loss

# Calculate the average change
average_change = sum(monthly_changes) / len(monthly_changes)

# Find the greatest increase and decrease in profits
max_increase = max(monthly_changes)
max_decrease = min(monthly_changes)

# Find the corresponding dates for the greatest increase and decrease
max_increase_date = dates[monthly_changes.index(max_increase)]
max_decrease_date = dates[monthly_changes.index(max_decrease)]

# Print the analysis results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")

# Save the analysis results to a text file
with open('PyBank_Solution', 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profit_losses}\n")
    txtfile.write(f"Average Change: ${round(average_change, 2)}\n")
    txtfile.write(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})\n")

# Print a message indicating where the results were saved
print("Results saved to 'PyBank_Solution.txt'")


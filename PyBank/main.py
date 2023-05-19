import os
import csv

budget_data_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

total_months = 0
net_total_profit_losses = 0
previous_profit_losses = 0
total_change = 0
average_changes_in_profit_losses = 0
greatest_increase_in_profits = 0
greatest_decrease_in_profits = 0
greatest_increase_in_months = ""
greatest_decrease_in_months = ""

with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)

    for row in csv_reader:
        month = row [0]
        profit_losses = int(row [1])

        total_months = total_months + 1
        
        net_total_profit_losses += profit_losses

        changes_over_months = profit_losses - previous_profit_losses
        
        total_change += changes_over_months
        
        if changes_over_months > greatest_increase_in_profits:
            greatest_increase_in_profits = changes_over_months
            greatest_increase_in_months = month
        elif changes_over_months < greatest_decrease_in_profits:
            greatest_decrease_in_profits = changes_over_months
            greatest_decrease_in_months = month

        previous_profit_losses = profit_losses 

average_changes_in_profits_losses = total_change / (total_months)

print("Financial Analysis")
print("------------------")
print(f"Total months: {total_months}")
print(f"Total: ${net_total_profit_losses}")
print(f"Average Change: ${average_changes_in_profits_losses:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_in_months},(${greatest_increase_in_profits})")
print(f"Greatest Decrease in Profits: {greatest_decrease_in_months},(${greatest_decrease_in_profits})")

output_file = os.path.join("PyBank", "analysis", "financial_analysis.txt")

output = f"Financial Analysis\n" \
         f"------------------\n" \
         f"Total months: {total_months}\n" \
         f"Total: ${net_total_profit_losses}\n" \
         f"Average Change: ${average_changes_in_profits_losses:.2f}\n" \
         f"Greatest Increase in Profits: {greatest_increase_in_months},(${greatest_increase_in_profits})\n" \
         f"Greatest Decrease in Profits: {greatest_decrease_in_months},(${greatest_decrease_in_profits})"

with open(output_file, 'w') as file:
    file.write(output)

print("Output written to financial_analysis.txt")


    

    




    
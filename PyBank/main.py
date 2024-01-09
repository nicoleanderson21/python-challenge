import os
import csv

csvpath = os.path.join('Resources/budget_data.csv')

months = 0
net_prof = 0

profit = []
monthly_change = []
date = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csvheader = next(csvfile)

    for row in csvreader:
        months = months + 1

        date.append(row[0])

        profit.append(int(row[1]))
        net_prof = sum(profit)

    for i in range(1, months):
        prof_change = profit[i]-profit[i-1]
        monthly_change.append(prof_change)

    avg_change = sum(monthly_change)/months
    rounded_avg = round(avg_change, 2)

    greatest_increase_prof = max(monthly_change)
    greatest_decrease_prof = min(monthly_change)

    increase_date = date[monthly_change.index(greatest_increase_prof)]
    decrease_date = date[monthly_change.index(greatest_decrease_prof)]

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(months)) 
print("Total: $" + str(net_prof))
print("Average Change: $" + str(float(rounded_avg)))
print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_prof) + ")")
print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_prof) + ")")

outFileName="../analysis/results.txt"
outFile=open(outFileName, "w")
outFile.write("Financial Analysis \n")
outFile.write("---------------------------- \n")
outFile.write("Total Months: " + str(months) + "\n") 
outFile.write("Total: $" + str(net_prof) + "\n")
outFile.write("Average Change: $" + str(float(rounded_avg)) + "\n")
outFile.write("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_prof) + ") \n")
outFile.write("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_prof) + ") \n")
outFile.close

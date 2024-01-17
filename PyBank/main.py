#starting off initializing and reading in the CSV file using code from activity 3-8
#initialize
from ast import If
import os
import csv

#set file path
csvpath = 'C:/Users/Eric/Downloads/python-challenge/PyBank/resources/budget_data.csv'

#open file
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    
    #running total number of months 
    months_total = int(0)
    #running count of net total amount of "Profit/Losses"
    net_prof = float(0)
    #greatest profit tracker value
    g_profit = float(0)
    #greatest loss tracker value
    g_loss = float(0)

    for row in csvreader:
        #get current profit/loss value
        currentval = float(row[1])
        #increase number of months
        months_total += 1
        #add change to net proft loss count
        net_prof += currentval

        #check if current value is a profit or a loss
        if currentval >= 0:
            #check if current profit is greater than greatest profit
            if currentval > g_profit:
                #update value and save the date
                g_profit = currentval
                g_p_date = row[0]
        else:
            #check if current loss is greater than greatest loss
            if currentval < g_loss:
                #update value and save the date
                g_loss = currentval
                g_l_date = row[0]
        

    #calculate average change
    avgchange = net_prof/months_total

#export results

output_path = 'C:/Users/Eric/Downloads/python-challenge/PyBank/analysis/output.txt'

with open(output_path, 'w') as f:
    f.write('Financial Analysis\n--------------\n')
    print('Financial Analysis\n--------------\n')
    f.write('Total Months: ' + str(months_total) + '\n')
    print('Total Months: ' + str(months_total) + '\n')
    f.write('Total: $' + str(net_prof) + '\n')
    print('Total: $' + str(net_prof) + '\n')
    f.write('Average change: $' + str(avgchange) + '\n')
    print('Average change: $' + str(avgchange) + '\n')
    f.write('Greatest increase in profits: ' + str(g_p_date) + ' $' + str(g_profit) + '\n')
    print('Greatest increase in profits: ' + str(g_p_date) + ' $' + str(g_profit) + '\n')
    f.write('Total decrease in profits: ' + str(g_l_date) + ' $' + str(g_loss) + '\n')
    print('Total decrease in profits: ' + str(g_l_date) + ' $' + str(g_loss) + '\n')
#import file

import os
import csv

#path to the csvfile

csvpath = os.path.join("/Users/karlaarzate/Desktop/Python-challenge/PyBank/Resources/budget_data.csv")

#declare the variables 
total_months = 0
total_profits =0
changes =[]
date_count = []
greatest_inc = 0
greatest_inc_month = 0
greatest_dec = 0
greatest_dec_month = 0

# Reading using CSV module
with open(csvpath) as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    next(csvreader, None)
    row = next(csvreader)
    
# months and total profits
    previous_profit = int(row[1])
    total_months = total_months + 1
    total_profits = total_profits + int(row[1])
    greatest_inc = int(row[1])
    greatest_inc_month = row[0]

    for row in csvreader:
 
        total_months = total_months + 1
        total_profits = total_profits + int(row[1])

        # change in months
        change = int(row[1]) - previous_profit
        changes.append(change)
        previous_profit = int(row[1])
        date_count.append(row[0])
        
        #greatest increase
        if int(row[1]) > greatest_inc:
            greatest_inc = int(row[1])
            greatest_inc_month = row[0]
            
        #greatest decrease
        if int(row[1]) < greatest_dec:
            greatest_dec = int(row[1])
            greatest_dec_month = row[0]  
      
    # average and date
    average_change = sum(changes)/len(changes)

    high = max(changes)
    low = min(changes)

    # Print Analysis 
    print("Financial Analysis")
    print("Total Months:" + str(total_months))
    print("Total Amount:" + str(total_profits))
    print(average_change)
    print(greatest_inc_month, max(changes))
    print(greatest_dec_month, min(changes))

#write new data

    PyBank = open("Financial Analysis.txt","w+")
    PyBank.write("Financial Analysis") 
    PyBank.write('\n' +"Total Months" + str(total_months)) 
    PyBank.write('\n' +"Total Amount" + str(total_profits)) 
    PyBank.write('\n' +"Average" + str(average_change)) 
    PyBank.write('\n' +greatest_inc_month) 
    PyBank.write('\n' +str(high))
    PyBank.write('\n' +greatest_dec_month) 
    PyBank.write('\n' +str(low))     
        
        
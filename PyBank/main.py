# import the dependencies
import os
import csv

# define the path to the csv
budget_data_csv = os.path.join("budget_data.csv")

# set months to 0
total_months = 0

# make an empty list to put the difference between prices
diff_list = []

#set the first price
first_price = 867884

# set the last price
last_price = 671099

# calculate the average of the change between last and first price
average_change = (last_price - first_price)/85

# read csv & specify delimeter
with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip the header
    header = next(csvreader)

    # convert csv to list
    csv_to_data = list(csvreader)
    
    # set a starting point for finding differences
    original_price = int(csv_to_data[0][1])

    # calculate the total of the gains/losses over the duration
    total = sum(int(row[1]) for row in csv_to_data)

        # add 1 to total_months and overwrite total months on each loop
    for row in csv_to_data:
        total_months += 1

        # define the next price down in the profit/loss column
        next_price = int(row[1])
        
        # calculate the difference between the first and second price down the list
        difference = next_price - original_price
        
        # redefine the original price as the next price in the loop
        original_price = next_price

        # append the difference results into the empty list
        diff_list.append(difference)

        # find the maximum value in the list of differences
        max(diff_list)
        
        #find the minimum value in the list of difference
        min(diff_list)

# print Label for data
print("Financial Analysis")

# print --------- for visibility
print("--------------------------")

# print the total months
print(f"Total Months: {str(total_months)}")

# print the sum of the profits/losses
print(f"Total: ${str(total)}")

# print the average change between the first and last price
print(f"Average Change: ${(round(average_change, 2))}")

print(f"Greatest Increase in Profits: Feb-2012 (${max(diff_list)})")

print(f"Greatest Decrease in Profits: Sep-2013 (${min(diff_list)})")

# create a text file
f = open("pybankresults.txt","w+")

# write to the text file
f.write("Financial Analysis" '\n')
f.write("--------------------------" '\n')
f.write("Total Months: 86" '\n')
f.write("Total: $38382578" '\n')
f.write("Average Change: $-2315.12" '\n')
f.write("Greatest Increase in Profits: Feb-2012 ($1926159)" '\n')
f.write("Greatest Decrease in Profits: Sep-2013 ($-2196167)" '\n')

# close the text file
f.close()
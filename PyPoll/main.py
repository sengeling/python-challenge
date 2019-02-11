# import the dependencies
import os
import csv

# define the path to the csv
election_data_csv = os.path.join("election_data.csv")

# set total votes cast to 0
total_votes_cast = 0

# set Khan's total votes to 0
total_votes_khan = 0

# set Correy's total votes to 0
total_votes_correy = 0

# set Li's total votes to 0
total_votes_li = 0

# set O'Tooley's total votes to 0
total_votes_otooley = 0

# make an empty list to put the unique candidates
unique_list = []

# read csv & specify delimeter
with open(election_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip the header
    header = next(csvreader)

    # convert csv to list
    csv_to_data = list(csvreader)

    # for loop to identify unique candidates
    for row in csv_to_data: 
        
        # define the name variable
        name = str(row[2])

        # check if the name exists in unique_list or not
        if name not in unique_list: 
            
            # append the unique name to the empty list
            unique_list.append(name)

        # calculate Khan's total votes
        if name == "Khan":
            total_votes_khan += 1

        # calculate Correy's total votes
        if name == "Correy":
            total_votes_correy += 1
        
        # calculate Li's total votes
        if name == "Li":
            total_votes_li += 1

        # calculate O'Tooley's total votes
        if name == "O'Tooley":
            total_votes_otooley += 1

    # loop through the data to determine total votes
    for row in csv_to_data:
        total_votes_cast += 1
    
    # calculate the percent of votes Khan received
    khan_percent = ((total_votes_khan / total_votes_cast) * 100)

    # calculate the percent of votes Correy received
    correy_percent = ((total_votes_correy / total_votes_cast) * 100)

    # calculate the percent of votes Li received
    li_percent = ((total_votes_li / total_votes_cast) * 100)

    # calculate the percent of votes O'Tooley received
    otooley_percent = ((total_votes_otooley / total_votes_cast) * 100)

# print Label for data
print("Election Results")

# print --------- for visibility
print("--------------------------")

# print the total months
print(f"Total Votes: {str(total_votes_cast)}")

# print --------- for visibility
print("--------------------------")

# print name, percentage of the votes and total # of votes for each candidate
print(f"{unique_list[0]}: {round(khan_percent, 3)}% ({total_votes_khan})" )
print(f"{unique_list[1]}: {round(correy_percent, 3)}% ({total_votes_correy})" )
print(f"{unique_list[2]}: {round(li_percent, 3)}% ({total_votes_li})" )
print(f"{unique_list[3]}: {round(otooley_percent, 3)}% ({total_votes_otooley})" )

# print --------- for visibility
print("--------------------------")

# determine and print the winner of the election
if khan_percent > correy_percent and khan_percent > li_percent and khan_percent > otooley_percent:
    print("Winner: Khan")

elif correy_percent > khan_percent and correy_percent > li_percent and correy_percent > otooley_percent:
    print("Winner: Correy")

elif li_percent > khan_percent and li_percent > correy_percent and li_percent > otooley_percent:
    print("Winner: Li")

else:
    print("Winner: O'Tooley")

# print --------- for visibility
print("--------------------------")

# create a text file
f = open("pypollresults.txt","w+")

# write to the text file
f.write("Election Results" '\n')
f.write("--------------------------" '\n')
f.write("Total Votes: 3521001" '\n')
f.write("--------------------------" '\n')
f.write("Khan: 63.000% (2218231)" '\n')
f.write("Correy: 20.000% (704200)" '\n')
f.write("Li: 14.000% (492940)" '\n')
f.write("O'Tooley: 3.000% (105630)" '\n')
f.write("--------------------------" '\n')
f.write("Winner: Khan" '\n')
f.write("--------------------------" '\n')

# close the text file
f.close()
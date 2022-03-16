# The data we need to retrieve
#Add our dependencies
import csv
import os

#assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter
total_votes = 0

#declare variable for candidate names
candidate_options = []


#Open the election results and read the file
with open(file_to_load) as election_data:

    #to do: Perform analysis (read and analyze data here.)
   # print(election_data)
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Print the header row
    headers = next(file_reader)
    #print(headers)

    #Print each row in the csv file
    for row in file_reader:
        #2. Add to the total vote count
        total_votes +=1

#3. Print the total votes
#print(total_votes)

# Print the candidate name from each row
        candidate_name = row[2]

#Add the candidate name to the candidate list
        if candidate_name not in candidate_options: 
                candidate_options.append(candidate_name)
        
#Print the candidate List
print(candidate_options)

#Close File (not needed when using with funtion)
#election_data.close()

#2. A complete list of candidates who received votes.
#3. The percentage of votes each candidate won.
#4. The total number of votes each candidate won.
#5. The winner of the election based on the popular vote. 


#Using the open() function with a "w" mode we will write data to the file. 
#open(file_to_save, "w")
#Use the open statement to open the file as a text file
with open (file_to_save, "w") as txt_file:

#Write some data to the file
# outfile.write("Hello World")
# outfile.close()
#Write three counties to the file
    # txt_file.write("Arapahoe, ")
    # txt_file.write("Denver, ")
    # txt_file.write("Jefferson")
    txt_file.write("Counties in the Election\n----------------\nArapahoe\nDenver\nJefferson")

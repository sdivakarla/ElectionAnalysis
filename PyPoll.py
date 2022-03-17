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
#declare empty dictionary for candidate votes
candidate_votes = {}
#Declare string for winning candidate
winning_candidate = ""
#declare variable for winning count
winning_count = 0
#Declare variable for winning percentage
winning_percentage = 0


#Open the election results and read the file
with open(file_to_load) as election_data:

    #to do: Perform analysis (read and analyze data here.)

    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Print the header row
    headers = next(file_reader)

    for row in file_reader:
        #2. Add to the total vote count
        total_votes +=1



# Print the candidate name from each row
        candidate_name = row[2]

#Add the candidate name to the candidate list
        if candidate_name not in candidate_options: 
                #Add candidate name to the candidate list
                candidate_options.append(candidate_name)

                #Begin tracking candidate's vote count
                candidate_votes[candidate_name] = 0

        #Add a vote to that condidate's count
        candidate_votes[candidate_name] +=1

#Save results to text file
with open (file_to_save, "w") as txt_file:

                #Print the final vote count to the terminal
        election_results = (
                f"\nElection Results\n"
                f"----------------------\n"
                f"Total Votes: {total_votes:,}\n"
                f"----------------------\n")
        
        #3. Print the total votes
        print(election_results, end="")

        #2. A complete list of candidates who received votes.
        #Iterate through the candidate list
        txt_file.write(election_results)
        for candidate_name in candidate_votes:
                #Retrieve vote count of a candidate
                #4. The total number of votes each candidate won.
                votes = candidate_votes[candidate_name]
                #3. The percentage of votes each candidate won.
                #Calculate vote percentage        
                vote_percentage = float(votes)/ float(total_votes) * 100
                # Print the candindate name and percentage of vote
                # print(f'{candidate_name}: received {vote_percentage:.1f}% of the vote.')
                candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
                print(candidate_results)
                txt_file.write(candidate_results)

                if (votes> winning_count) and (vote_percentage > winning_percentage):
                        #If true then set winning_count = votes and winning_percentage = vote_percentage
                        winning_count = votes
                        winning_percentage = vote_percentage
                        #And set winning_candidate equal to candidate name
                        winning_candidate = candidate_name

        #5. The winner of the election based on the popular vote. 
        winning_candidate_summary = (
                f"---------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:1f}%\n"
                f"----------------------\n")
        print(winning_candidate_summary)

        #Save the final vote count to the text file
        txt_file.write(winning_candidate_summary)        

#Close File (not needed when using with funtion)
#election_data.close()

#Use the open statement to open the file as a text file
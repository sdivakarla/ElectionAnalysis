# Election Analysis
Election Analysis in Python

# Overview of the Election Audit

Our clients, Seth and Tom, have election data from Colorado and have requested analysis of the results. They have requested algorithums to evaluate the results. Seth prefers to run code from the command line and would like results printed to the terminal. Resuls also need to be sent to a text file. The election audit will take data from a comma seperated values (csv) file with over 300,000 votes and summarize the data.  The results will indicate the winner as well as some county specific information so Seth and Tom can see where votes were cast. 

# Election Audit Results

The file with the election data was analyzed to determine the following information: 

1. Number of votes cast in this congressional election: 369,711. 
2. Number of votes and percentage of total votes in each county
*   Jefferson County (38,855 votes for 10.5% of the total vote)
*   Denver County  (306,055 votes for 82.8% of the total vote)
*   Arapahoe County (24,801 votes for 6.7% of the total vote)
3. County with the largest number of votes: Denver
4. Number of votes and percentage of total votes for each candidate: 
*   Charles Casper Stockham received 85,213 votes for 23.0% of the total. 
*   Diana DeGette received 272,892 votes for 73.8% of the total.
*   Rayman Anthony Doane received 11,606 votes for 3.1% of the total. 
5. Diana DeGette was the winner of the election with 73.8% of the total and 272,892 votes. 

 The results were sent to a text file:
 
 ![ElectionResultsTxt](https://user-images.githubusercontent.com/98054953/159175045-154a6a73-80eb-41e9-bcaf-798ba943237d.png)

# Election Audit Summary 

The ability to convert the data file (provided in csv format) to a readable summary is a valuable tool to support the election audit committee. The script written for the analysis can be modified to provide election analysis for any election.  This election had data according to county and individual candidates.  For future elections, the script could be modified according to the data collected.  If the election is based on precints or has multiple candidates, an update to the code would allow for similar summary statements and analysis. It would also be possible to determine the winning candidate in each county if that was useful information. 

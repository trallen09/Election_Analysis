# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.basename("election_results.csv")
print(file_to_load)

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0
# Candidate Options List
candidate_options = []
# Declare empty dictionary
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
   
    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes = total_votes + 1

        #Print the candidate name for each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate in the candidate_options list at the top
        if candidate_name not in candidate_options:
            #Add the candidate name to the candiate list.
            candidate_options.append(candidate_name)
            # 2 Begin tracking that candidate's vote count to empty delcared dictionary. This specifies key inside [] and sets value.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
print(candidate_votes)        

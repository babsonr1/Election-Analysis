#file_to_load = 'election_results.csv'
#election_data = open(file_to_load, 'r')

#with open(file_to_load) as election_data:
  #  print(election_data)

import csv
import os.path
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("..", "Resources", "election_results.csv")
file_to_save = os.path.join("..", "Resources", "Analysis", "Election Analysis.txt")
#variables needed
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
  file_reader = csv.reader(election_data)

  #determining the headers
  headers = next(file_reader)
  
  #for each row count the votes and find the candidates
  for row in (file_reader):
    total_votes += 1
    candidate_name = row[2]

    #only add candidate name if it is not in the options already
    if candidate_name not in candidate_options:
      candidate_options.append(candidate_name)
      candidate_votes[candidate_name] = 0
    
    #assigning votes to the correct candidates
    candidate_votes[candidate_name] += 1

#find the votes and percantages of each candidate
for candidate_name in candidate_votes:
  votes = candidate_votes[candidate_name]
  vote_percentage = float(votes) / float(total_votes) * 100
  print(f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")

  #determining who had the most votes
  if (votes > winning_count) and (vote_percentage > winning_percentage):
    winning_count = votes
    winning_candidate = candidate_name
    winning_percentage = vote_percentage
winning_candidate_summary = (
  f"--------------------\n"
  f"Winner: {winning_candidate}\n"
  f"Winning Vote Count: {winning_count:,} \n"
  f"Winning Percentage: {winning_percentage:.1f}%\n"
  f"--------------------\n"
)
print(winning_candidate_summary)


    
print(total_votes)
print(candidate_votes)

  
    

with open(file_to_save, "w") as outfile:
  outfile.write(str(headers))


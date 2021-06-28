#file_to_load = 'election_results.csv'
#election_data = open(file_to_load, 'r')

#with open(file_to_load) as election_data:
  #  print(election_data)

import csv
import os.path
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("..", "Resources", "election_results.csv")
file_to_save = os.path.join("..", "Resources", "Analysis", "Election Analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:
  file_reader = csv.reader(election_data)

  headers = next(file_reader)
  print(headers)

  
    

with open(file_to_save, "w") as outfile:
  outfile.write(str(headers))


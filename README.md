# Election-Analysis
## Overview
---
#### The purpose of this exercise was to give Seth and Tom a rundown of election results in three counties, Arapahoe, Denver, and Jefferson. This scenario was used to explore Python and GitBash to create code and upload it remotely without going on the GitHub website. Voter counts, percentages, and winners were calculated using Python-coding methodologies.
## Election Audit Results
- There were 369711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote with a count of 85,213 votes.
  - Diana DeGette received 73.8% of the vote with a count of 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote with a count of 11,606 votes.
- The winner of the election was Diana DeGette, who received 73.8% of the vote with a count of 272,892 votes.
- The counties were:
  - Arapahoe
  - Denver
  - Jefferson
- The county results were:
  - Arapahoe contributed 6.7% of the vote with a count of 24,801 votes.
  - Denver contributed 82.8% of the vote with a count of 306,055 votes.
  - Jefferson contributed 10.5% of the vote with a count of 38,855 votes.
- The biggest voter percentage was from Denver with 82.8% of the vote at 306,055 votes.
## Election Audit Summary
The winning candidate was Diane DeGette in this small scale application of election results with 73.8% of the votes. This project could be emulated with much more data by changing a few things.

One thing that has to be sure to be changed is:
`candidate_name = row[2]` and `county_name = row[1]`.
It happened to be in this election results file that the names were in row 3 and the counties were in row 2, so they were indexed at 2 and 1, respectively, but this is not necessarily the case with all files.

Another thing that could be added would be another form of analysis. For example,  in this case, only candidates and counties were looked at, but wealthiness, party affiliation, and many other demographics could be looked at. In this case, something like the below code could be added to tally that information.
```
if demographic_name not in demographic_options:

   # Add the demographic name to the demographic list.
   demographic_options.append(demographic_name)

   # And begin tracking that demographic's voter count.
   demographic_votes[demographic_name] = 0

# Add a vote to that demographic's count
demographic_votes[demographic_name] += 1
``` 

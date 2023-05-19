import os
import csv

election_data_csv = os.path.join("PyPoll","Resources","election_data.csv")

total_votes = 0
candidate_votes = {}

with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)

    for row in csv_reader:
        total_votes = total_votes + 1

        candidate_name = row[2]

        candidate_votes[candidate_name] = candidate_votes.get(candidate_name, 0) + 1

candidates = list(candidate_votes.keys())

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate in candidates:
    votes = candidate_votes.get(candidate, 0)
    vote_percentage = (votes / total_votes) * 100
    print("{}: {:.3f}% ({})".format(candidate, vote_percentage, votes))

print("-------------------------")

winner = max(candidate_votes, key=candidate_votes.get)
print(f"Winner: {winner}")

print("-------------------------")

output_file = os.path.join("PyPoll", "analysis", "election_data_results")

output = f"Election Results\n" \
         f"-------------------------\n" \
         f"Total Votes: {total_votes}\n" \
         f"-------------------------\n" \
         
for candidate in candidates:
    votes = candidate_votes.get(candidate, 0)
    vote_percentage = (votes / total_votes) * 100
    output += f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

output += "-------------------------\n" \
          f"Winner: {max(candidate_votes, key=candidate_votes.get)}\n" \
          "-------------------------\n"

with open(output_file, 'w') as file:
    file.write(output)

print("Output written to election_results.txt")
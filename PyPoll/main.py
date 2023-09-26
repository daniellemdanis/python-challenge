import os
import csv

csvpath = os.path.join('.','Resources','election_data.csv')

# Initialize variables to store analysis results
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

# Read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    
    # Skip the header row
    next(csvreader)

    for row in csvreader:
        # Extract the candidate name from the current row
        candidate = row[2]

        # Update the total number of votes
        total_votes += 1

        # Update the candidate's vote count
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Calculate the percentage of votes and find the winner
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    candidates[candidate] = {
        "votes": votes,
        "percentage": round(percentage, 2),
    }

    # Determine the winner
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Print the analysis results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, data in candidates.items():
    print(f"{candidate}: {data['percentage']}% ({data['votes']})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Save the analysis results to a text file
with open('PyPoll_Solution.txt', 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate, data in candidates.items():
        txtfile.write(f"{candidate}: {data['percentage']}% ({data['votes']})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")

# Print a message indicating where the results were saved
print("Results saved to 'PyPoll_Solution.txt'")

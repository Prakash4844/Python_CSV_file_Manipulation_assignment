# Output Leaderboard for the users based on the number of statements they have made.
import csv

users = []
with open('input_sheet_2.csv', 'r') as f:
    next(f)  # skip header row
    for line in f:
        s_no, name, uid, statements, reasons = line.strip().split(',')
        users.append((name, int(uid), int(statements), int(reasons)))  # add this line to initialize the
        # list for each user with (name, uid, statements, reasons) as tuple in the list.

# Sort users by number of statements in descending order,the key is the 3rd element in the every tuple that
# is stored in list users.
user_ranks = sorted(users, key=lambda x: x[2], reverse=True)

# Save user leaderboard to a CSV file
with open('user_leaderboard_2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Rank', 'Name', 'UID', 'No. of Statements', 'No. of Reasons'])
    for rank, (name, uid, statements, reasons) in enumerate(user_ranks, start=1):
        writer.writerow([rank, name, uid, statements, reasons])

print("Output written to user_leaderboard_2.csv")

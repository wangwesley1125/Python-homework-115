'''
Write a script that uses a dictionary to determine the number of
votes received by candidates in an election. The votes are concatenated in a string where
each vote is separated from the next by a comma. Use the techniques you learned in
Section 6.2.7. [Hint: split can take in an argument for the specific delimiter you wish to
use in a string.]

votes="mary,tom,tom,mary,john,mary,tom,john,john,mary"
using dictionary

'''

votes = "mary,tom,tom,mary,john,mary,tom,john,john,mary"

vote_count = {}

for vote in votes.split(','):
    if vote in vote_count:
        vote_count[vote] += 1
    else:
        vote_count[vote] = 1

print(f"{"Candidate": <10} VOTES")

for vote, count in sorted(vote_count.items()):
    print(f"{vote: <10} {count}")
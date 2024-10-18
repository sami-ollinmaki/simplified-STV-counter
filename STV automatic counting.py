DEBUG = False


import math
from random import getrandbits as rand

def counting_round(votes:list):
    # Add every candidate to dict
    vote_counts = {}
    for candidate in votes[1]:
        if not candidate == '':
            vote_counts[candidate] = 0

    # Count the "active" vote of each ballot
    for i in votes:
        if not i[0] == '':
            vote_counts[i[0]] += 1

    return vote_counts

def eliminate_candidate(votes:list, candidate:str):
    newVotes = []

    for l in votes:
        if not candidate in l:
            newVotes.append(l)
        else:
            l.remove(candidate)
            newVotes.append(l)
    return newVotes

def count_votes():
    votes = []
    hasRandom = False

    # Pull voting data from file and store it in a list by ballot
    with open(file_location) as file:
        for row in file:
            row = row.strip('\n')
            row = row.split(';')
            votes.append(list(filter(None, row)))

    # Calculate quota as Droop quota
    quota = math.floor(len(votes) / (1 + 1)) + 1

    # Repeat vote counting and elimination until a candidate has reached the quota
    while True:
        # Perform a counting round and store the results in a dictionary
        vote_counts = counting_round(votes)

        # From the dictionary get the most and least voted candidate
        # If there are more than one with the same amount of votes, decide between them randomly
        # NOTE: This could be improved, where it could for example look at the previous results to determine who to keep, maybe a TODO for the future
        # This however is not a significant problem with the intended use case, where the data is far from even and there aren't many candidates
        most_votes = '',0
        least_votes = '',9999999
        for k,v in vote_counts.items():
            if v == most_votes[1]:
                hasRandom = True
                if rand(1):
                    most_votes = k,v
            if v > most_votes[1]:
                most_votes = k,v

            if v == least_votes[1]:
                hasRandom = True
                if rand(1):
                    least_votes = k,v
            if v < least_votes[1]:
                least_votes = k,v

        # Test if the candidate with the most votes exceeds the quota for being choses
        # Note that as only one candidate is being chosen, the quota will always be above 50% and as such there cannot be more than one candidate who exceeds it
        if most_votes[1] >= quota:
            return most_votes, hasRandom
        
        # If no candidate exceeds the quota, eliminate the worst candidate from everyones ballot and repeat
        votes = eliminate_candidate(votes, least_votes[0])


## Runtime operation
if __name__ == '__main__':
    ## Initial instructions for the usage of this script
    print("All of the valid votes must be in an CSV file. Different votes must be separated with a line change")
    print("In a single vote the data should be organized from most to least favorite, values being separated by a semi-colon (;).")
    print()
    print("Example for a votes's data, if the candidates are called A, B and C:")
    print("     C;A;B;")
    print()
    print("To achieve this data, you can for example put just the voting data in an Excel spreadsheet on different rows and export it as CSV")
    print()
    print()



    if DEBUG:
        file_location = 'TestData2.csv'
    else:
        file_location = input("Input path of the .csv file that contains the voting data: ")

    print("Voting data:")
    with open(file_location) as file:
        for row in file:
            row = row.strip('\n')
            print(f"    {row}")
    file.close()

    if not input("Is this data correct? (y/n): ") == 'n':
        winner, hasRandom = count_votes()

        if winner:
            print(f"{winner[0]} has the most votes at {winner[1]} and should be elected! ", end="")
            if hasRandom:
                print("Randomness was used in deciding the outcome. Rerunning the code may change the result. As such, code SHOULD NOT BE RERUN.")
        else:
            print(f"No winner could be decided! Check votes manually")
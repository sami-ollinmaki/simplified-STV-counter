from string import ascii_uppercase
from random import shuffle

votes = []
candAmount = 10
voteAmount = 250

candidates = list(ascii_uppercase[0:candAmount])

for i in range(voteAmount):
    shuffle(candidates)
    votes.append(';'.join(candidates))


with open('TestData3.csv','w') as file:
    file.write('\n'.join(votes))    
# import dependecies
import csv

# define variables
votes = []
charles = 'Charles Casper Stockham'
diana = 'Diana DeGette'
raymon = 'Raymon Anthony Doane'
charles_v = 0
diana_v = 0
raymon_v = 0
winner = ''

# open file
with open('./Resources/election_data.csv', encoding='UTF-8') as csvfile:
    pointer = csv.reader(csvfile)
    next(pointer)

    for x in pointer:
        votes.append(x[0])
        if (x[2]) == charles:
            charles_v += 1
        elif (x[2]) == diana:
            diana_v += 1
        else:
            raymon_v += 1
            
p_c = round((charles_v*100)/len(votes), 3)
p_d = round((diana_v*100)/len(votes), 3)
p_r = round((raymon_v*100)/len(votes), 3)

if charles_v > diana_v and charles_v > raymon_v:
    winner = charles
elif diana_v > charles_v and diana_v > raymon_v:
    winner = diana
else:
    winner = raymon

# print to terminal
print(f'Election Results')
print(f'------------------------')
print(f'Total Votes: {len(votes)}')
print(f'------------------------')
print(f'{charles}: {p_c}% ({charles_v})')
print(f'{diana}: {p_d}% ({diana_v})')
print(f'{raymon}: {p_r}% ({raymon_v})')
print(f'------------------------')
print(f'Winner: {winner}')
print(f'------------------------')

# output to file
output = open("./analysis/Analysis.txt", 'w')
output.write(f'''
Election Results
------------------------
Total Votes: {len(votes)}
------------------------
{charles}: {p_c}% ({charles_v})
{diana}: {p_d}% ({diana_v})
{raymon}: {p_r}% ({raymon_v})
------------------------
Winner: {winner}
------------------------''')
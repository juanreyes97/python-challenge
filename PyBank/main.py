# import dependecies
import csv

# define variables
total_months = []
total_ = []
totalChange = []
avg_change = 0
total_change = 0
minimum_ = 0
maximum_ = 0 
datemax = ''
datemin = ''

# open file
with open('./Resources/budget_data.csv', encoding='UTF-8') as csvfile:
    pointer = csv.reader(csvfile)
    next(pointer)
    for x in pointer:
        total_months.append(x[0])
        total_.append(int(x[1]))
        total_change = (-(avg_change) + (float(x[1])))
        avg_change = (float(x[1]))
        totalChange.append(total_change)

        if maximum_ > total_change:
            maximum_ = maximum_
        else:
            maximum_ = total_change
            datemax = x[0]

        if minimum_ < total_change:
            minimum_ = minimum_
        else:
            minimum_ = total_change
            datemin = x[0]

del totalChange[0]
totalMonths = len(total_months)
total = sum(total_)
avgChange = round(sum(totalChange)/len(totalChange), 2)
maximum = int(max(totalChange))
minimum = int(min(totalChange))

# print to terminal
print(f'Financial Analysis')
print(f'------------------')
print(f'Total Months: {totalMonths}')
print(f'Total Amount: ${total}')
print(f'Average Monthly Change: ${avgChange}')
print(f'Greatest Increase in Profits: {datemax} (${maximum})')
print(f'Greatest Decrease in Profits: {datemin} (${minimum})')

# output to file
output = open("./analysis/Analysis.txt", 'w')
output.write(f'''
Financial Analysis
------------------
Total Months: {totalMonths}
Total: ${total}
Average Monthly Change: ${avgChange}
Greatest Increase in Profits: {datemax} (${maximum})
Greatest Decrease in Profits: {datemin} (${minimum})''')
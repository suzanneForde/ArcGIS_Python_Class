
###
# Part 3
###

import csv

with open("co2_ML.csv") as population_csv:
    next(population_csv) #skip first line
    total = 0
    for row in csv.reader(population_csv):
        total += float(row[1])
    print(format(total, 'f'))
    print(total)




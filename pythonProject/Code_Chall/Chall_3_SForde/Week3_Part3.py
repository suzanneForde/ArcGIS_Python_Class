
###
# Part 3
###

import csv


with open("co2_ML.csv") as population_csv:
    csv_reader = csv.reader(population_csv, delimiter=',')

    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            print("Column names are: " + str(row))
            line_count += 1
        line_count += 1

print("Processed " + str(line_count) + " lines.")

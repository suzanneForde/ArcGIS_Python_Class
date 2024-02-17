
###
# Part 3
###

import csv

## 1. Annual average for each year in the dataset.

years = []
sums_pyear = []

with open("co2_ML.csv") as year_csv:
    next(year_csv)
    total = 0
    for row in csv.reader(year_csv):
        years.append(row[0])
        sums_pyear.append(row[1])
print(years)
print(sums_pyear)

    #     total += float(row[1])
    # print(format(total, 'f'))
    # print(total)

## 2. Minimum, maximum and average for the entire dataset.


## 3. Seasonal average if Spring (March, April, May), Summer (June, July, August),
## Autumn (September, October, November) and Winter (December, January, February).




## 4. Calculate the anomaly for each value in the dataset relative to the mean for the entire time series.


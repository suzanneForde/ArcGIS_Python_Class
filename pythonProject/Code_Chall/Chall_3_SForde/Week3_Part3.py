
###
# Part 3
###

import csv

## 1. Annual average for each year in the dataset.

years = []

for year in years:
    with open('c02_ML.csv') as year_csv:
        saved_header = next(year_csv)
        file = open(r"throwaway\" + years + ".txt", "w")
        file.write(saved_header)
        for row in csv.reader(year_csv):
            if years == row[0]:
                file.write(row)
        file.close()



# year_total += float(row[2])
#
# print(years)


## 2. Minimum, maximum and average for the entire dataset.


## 3. Seasonal average if Spring (March, April, May), Summer (June, July, August),
## Autumn (September, October, November) and Winter (December, January, February).




## 4. Calculate the anomaly for each value in the dataset relative to the mean for the entire time series.


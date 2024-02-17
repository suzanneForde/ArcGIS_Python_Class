
###
# Part 3
###


## 1. Annual average for each year in the dataset.

import csv
import datetime

with open('co2_ML.csv') as csvfile:
    reader = csv.DictReader(
        csvfile, fieldnames=('date', 'stations', 'pcp'), delimiter=',', quotechar='|')
    next(reader)
    x = [row['date'] for row in reader]

for date_str in x:
    month, day, year = date_str.split('/')
    print(month, day, year)



## 2. Minimum, maximum and average for the entire dataset.


## 3. Seasonal average if Spring (March, April, May), Summer (June, July, August),
## Autumn (September, October, November) and Winter (December, January, February).




## 4. Calculate the anomaly for each value in the dataset relative to the mean for the entire time series.


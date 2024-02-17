
###
# Part 3
# o my lord this was hell
###


## 1. Annual average for each year in the dataset.

import csv
import datetime

year_total = {}
year_count = {}
annual_averages = {}
def calculate_annual_average(data):
    for row in data:
        date_parts = row[0].split('/')
        if len(date_parts) < 3:
            print("Invalid date format:", row[0])
            continue

        year = date_parts[2]
        value = float(row[1])

        if year in year_total:
            year_total[year].append(value)
            year_count[year] += 1
        else:
            year_total[year] = [value]
            year_count[year] = 1


    for year in year_total:
        annual_averages[year] = sum(year_total[year]) / year_count[year]

    return annual_averages

data = []
with open('co2_ML.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        data.append(row)

annual_averages = calculate_annual_average(data)

for year, average in annual_averages.items():
    print(f'Year {year}: {average}')



## 2. Minimum, maximum and average for the entire dataset.
def calculate_stats(data):
    min_value = float('inf')
    max_value = float('-inf')
    sum_values = 0
    count = 0

    for row in data:
        value = float(row[1])
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value
        sum_values += value
        count += 1

    if count > 0:
        average = sum_values / count
    else:
        average = 0

    return min_value, max_value, average

data = []
with open('co2_ML.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        data.append(row)

min_value, max_value, average = calculate_stats(data)

print(f"Minimum: {min_value}")
print(f"Maximum: {max_value}")
print(f"Average: {average}")

## 3. Seasonal average if Spring (March, April, May), Summer (June, July, August),
## Autumn (September, October, November) and Winter (December, January, February).
def calculate_seasonal_average(data):
    seasonal_totals = {'Spring': 0, 'Summer': 0, 'Autumn': 0, 'Winter': 0}
    seasonal_counts = {'Spring': 0, 'Summer': 0, 'Autumn': 0, 'Winter': 0}
    def get_season(month):
        if 3 <= month <= 5:
            return 'Spring'
        elif 6 <= month <= 8:
            return 'Summer'
        elif 9 <= month <= 11:
            return 'Autumn'
        else:
            return 'Winter'

    for row in data:
        date_parts = row[0].split('/')
        if len(date_parts) < 3:
            print("Invalid date format:", row[0])
            continue

        month = int(date_parts[1])

        season = get_season(month)

        value = float(row[1])
        seasonal_totals[season] += value
        seasonal_counts[season] += 1

    seasonal_averages = {}
    for season in seasonal_totals:
        if seasonal_counts[season] > 0:
            seasonal_averages[season] = seasonal_totals[season] / seasonal_counts[season]
        else:
            seasonal_averages[season] = 0

    return seasonal_averages

data = []
with open('co2_ML.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        data.append(row)

seasonal_averages = calculate_seasonal_average(data)

for season, average in seasonal_averages.items():
    print(f"{season} Average: {average}")

## 4. Calculate the anomaly for each value in the dataset relative to the mean for the entire time series.
def calculate_mean(data):
    total_sum = 0
    total_count = 0
    for row in data:
        total_sum += float(row[1])
        total_count += 1
    if total_count == 0:
        return None
    return total_sum / total_count


def calculate_anomalies(data):
    mean = calculate_mean(data)
    if mean is None:
        print("Error: Cannot calculate anomaly, dataset is empty.")
        return None

    anomalies = []
    for row in data:
        value = float(row[1])
        anomaly = value - mean
        anomalies.append(anomaly)

    return anomalies


data = []
with open('co2_ML.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        data.append(row)

anomalies = calculate_anomalies(data)

if anomalies is not None:
    for i, anomaly in enumerate(anomalies):
        print(f"Anomaly for value {i + 1}: {anomaly}")

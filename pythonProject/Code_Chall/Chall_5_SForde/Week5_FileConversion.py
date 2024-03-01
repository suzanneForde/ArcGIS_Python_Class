
# pandas is a python library that can be used to work with data sets
import pandas as pd
import os


# Converting occurence.txt into a .csv file for week 5 challenge

# OTTER PUP OCCURRENCE

# First step is finding delimiter value
otter_pup_occurrence = r'C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Code_Chall\Chall_5_SForde\Species_Data\otter_female_pup_occurrence.txt'

def find_delimiter(otter_pup_occurrence):
    # Reads first lines of file
    with open(otter_pup_occurrence, 'r') as file:
        lines = [file.readline().strip() for _ in range(5)]

    # Defining potential delimiters
    delimiters = ['\t', ';', '[', '{', ']', '}', ':', '<', '>', '/']

    # Counting occurrences of potential delimiters
    delimiter_counts = {delimiter: sum(line.count(delimiter) for line in lines) for delimiter in delimiters}

    # Find the delimiter with the highest count
    max_delimiter = max(delimiter_counts, key=delimiter_counts.get)
    max_count = delimiter_counts[max_delimiter]

    return max_delimiter, max_count


# Finding the delimiter
delimiter, count = find_delimiter(otter_pup_occurrence)
print(f"The delimiter in the female otter and pup data file is '{delimiter}' with {count} occurrences.")



# POLAR BEAR OCCURRENCE
polar_bear_occurrence = r'C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Code_Chall\Chall_5_SForde\Species_Data\bear_dens_occurrence.txt'

def find_delimiter(polar_bear_occurrence):
    # Reads first lines of file
    with open(polar_bear_occurrence, 'r') as file:
        lines = [file.readline().strip() for _ in range(5)]

    # Defining potential delimiters
    delimiters = ['\t', ';', '[', '{', ']', '}', ':', '<', '>', '/']

    # Counting occurrences of potential delimiters
    delimiter_counts = {delimiter: sum(line.count(delimiter) for line in lines) for delimiter in delimiters}

    # Find the delimiter with the highest count
    max_delimiter = max(delimiter_counts, key=delimiter_counts.get)
    max_count = delimiter_counts[max_delimiter]

    return max_delimiter, max_count


# Finding the delimiter
delimiter, count = find_delimiter(polar_bear_occurrence)
print(f"The delimiter in the polar bear den data file is '{delimiter}' with {count} occurrences.")


# Setting workspace OTTER PUPS
otter_pups_input1 = r'C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Code_Chall\Chall_5_SForde\Species_Data\otter_female_pup_occurrence.txt'

otter_pups_csv = r'C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Code_Chall\Chall_5_SForde\Species_Data\otter_female_pups.csv'


try:
    df=pd.read_csv(otter_pups_input1, sep='\t')
    df.to_csv(otter_pups_csv, index=False)
except Exception as e:
    print("Error", e)

if os.path.isfile(otter_pups_csv):
    print("CSV file exists")
else:
    print("CSV file does not exist")


# Setting workspace POLAR BEARS
otter_pups_input1 = r'C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Code_Chall\Chall_5_SForde\Species_Data\bear_dens_occurrence.txt'

otter_pups_csv = r'C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Code_Chall\Chall_5_SForde\Species_Data\bear_dens.csv'


try:
    df=pd.read_csv(otter_pups_input1, sep='\t')
    df.to_csv(otter_pups_csv, index=False)
except Exception as e:
    print("Error", e)

if os.path.isfile(otter_pups_csv):
    print("CSV file exists")
else:
    print("CSV file does not exist")



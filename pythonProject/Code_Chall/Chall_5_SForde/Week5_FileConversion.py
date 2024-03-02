
# Data collected from GBIF | Global Biodiversity Information Facility
# https://www.gbif.org/dataset/a28eb0fc-73f3-471e-b927-cc58f576c9e0
# https://www.gbif.org/dataset/c911249c-5bdc-4847-8653-d7b81f11b7cc


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

import os
import csv

# OTTER PUP FILE COLUMN DELETION
otter_pup_FIRST =  r'C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Code_Chall\Chall_5_SForde\Species_Data\otter_female_pups.csv'
otter_pup_SECOND = r'C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Code_Chall\Chall_5_SForde\Species_Data\ot_pups_deleted_col.csv'

# specifying columns to be deleted
columns_to_delete = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 76, 77, 78]

# opening files to be modified
with open(otter_pup_FIRST, 'r', newline='') as infile, \
        open(otter_pup_SECOND, 'w', newline='') as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        modified_row = [row[i] for i in range(len(row)) if i not in columns_to_delete]
        writer.writerow(modified_row)
print('Columns deleted. otter_pup_second CSV file created.')


# Code so that python can read over the created .csv file
file_path = r'C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Code_Chall\Chall_5_SForde\Species_Data\ot_pups_deleted_col.csv'
ot_pu_CSV = os.path.basename(file_path)

if not os.path.exists(file_path):
    # File does not exist, create it
    with open(file_path, "w") as file:
        file.write("This is a new file.")
    print(f"File '{ot_pu_CSV}' created successfully.")
else:
    print(f"File '{ot_pu_CSV}' already exists. Not creating it.")

# POLAR BEAR FILE COLUMN DELETION
import csv

polar_bear_INPUT =  r'C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Code_Chall\Chall_5_SForde\Species_Data\bear_dens.csv'
polar_bear_OUTPUT = r'C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Code_Chall\Chall_5_SForde\Species_Data\deleted_bear_den_columns.csv'
#
columns_to_del = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25]

with open(polar_bear_INPUT, 'r', newline='') as infile, \
        open(polar_bear_OUTPUT, 'w', newline='') as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        modified_row2 = [row[i] for i in range(len(row)) if i not in columns_to_del]
        writer.writerow(modified_row2)
print('Columns deleted. deleted_bear_den_columns CSV file created.')

# Code so that python can read over the created .csv file
file_path2 = r'C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Code_Chall\Chall_5_SForde\Species_Data\deleted_bear_den_columns.csv'
po_bo_CSV = os.path.basename(file_path2)

if not os.path.exists(file_path):
    # File does not exist, create it
    with open(file_path, "w") as file:
        file.write("This is a new file.")
    print(f"File '{po_bo_CSV}' created successfully.")
else:
    print(f"File '{po_bo_CSV}' already exists. Not creating it.")
######################################


# Merging datasets

import os

if not os.path.exists('merged_species_file.csv'):
    import pandas as pd
    workspace = r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Code_Chall\Chall_5_SForde\Species_Data"

    bear_file_path = os.path.join(workspace, "deleted_bear_den_columns.csv")
    otter_file_path = os.path.join(workspace, "ot_pups_deleted_col.csv")


    df1 = pd.read_csv(bear_file_path)
    df2 = pd.read_csv(otter_file_path)

    # Merge the two dataframes
    merged_df = pd.concat([df1, df2], ignore_index=True)

    # Write the merged dataframe to a new CSV file
    merged_file_path = os.path.join(workspace, 'merged_species_file.csv' )
    merged_df.to_csv(merged_file_path, index=False)

    print("Merged data saved successfully.")
else:
    print("Merged species .csv already exists. Skipping process.")



# Data collected from GBIF | Global Biodiversity Information Facility
# https://www.gbif.org/dataset/a28eb0fc-73f3-471e-b927-cc58f576c9e0
# https://www.gbif.org/dataset/c911249c-5bdc-4847-8653-d7b81f11b7cc

# CSV conversion from txt file is in Week5_FileConversion.py


# Generate heatmaps for TWO species in Python.
#
# Requirements are:
# The two input species data must be in a SINGLE CSV file, you must process the input data to separate out the species
# (Hint: You can use a slightly edited version of our CSV code from a previous session to do this),
# I recommend downloading the species data from the same source so the columns match.
# Only a single line of code needs to be altered (workspace environment) to ensure code runs on another computer,
# and you provide the species data along with your Python code.
# The heatmaps are set to the right size and extent for your species input data, i.e. appropriate fishnet cellSize.
# You leave no trace of execution, except the resulting heatmap files.
# You provide print statements that explain what the code is doing, e.g. Fishnet file generated.
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


# Code so that I can overwrite the created .csv file
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

columns_to_del = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25]

with open(polar_bear_INPUT, 'r', newline='') as infile, \
        open(polar_bear_OUTPUT, 'w', newline='') as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        modified_row2 = [row[i] for i in range(len(row)) if i not in columns_to_del]
        writer.writerow(modified_row2)
print('Columns deleted. deleted_bear_den_columns CSV file created.')

# Code to overwrite polar bear csv creation
file_path2 = r'C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Code_Chall\Chall_5_SForde\Species_Data\deleted_bear_den_columns.csv'
po_bo_CSV = os.path.basename(file_path2)

if not os.path.exists(file_path):
    # File does not exist, create it
    with open(file_path, "w") as file:
        file.write("This is a new file.")
    print(f"File '{po_bo_CSV}' created successfully.")
else:
    print(f"File '{po_bo_CSV}' already exists. Not creating it.")



# import arcpy
# arcpy.env.workspace = r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Class_05"
#
# arcpy.env.overwriteOutput = True
#
# in_Table = r"Step_1_Deep_Coral.csv"
# x_coords = "decimalLongitude"
# y_coords = "decimalLatitude"
# z_coords = ""
# out_Layer = "deepcoral"
# saved_Layer = r"Step_1_Deep_Coral_Output.shp"
#
# spRef = arcpy.SpatialReference(4326)  # 4326 == WGS 1984
#
# lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)
# #
# # ##### 2. Print the count of the number of records in the file. (Hint: see above!)
# # # https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/get-count.htm
# #
# print(arcpy.GetCount_management(out_Layer))
# #
# # ##### 3. Check the correct coordinate system has been applied (Hint: see last week!)
# #
# arcpy.CopyFeatures_management(lyr, saved_Layer)
# #
# if arcpy.Exists(saved_Layer):
#     print("Created file successfully!")
#
# desc = arcpy.Describe(saved_Layer)
# print(desc.spatialReference.name)
#
# ##### 4. Visualize the file in ArcPro by dragging it into the program.
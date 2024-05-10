
#####
# Step 1 - Searching directories for files and list them
#####

# Handling files is a critical part of any GIS (and analysis) workflow. This is particularly true if you are
# working with large amounts of files as we often do. In this step, we cover several ways of searching and
# listing files. We will use a mix of different methods and packages to do this. There are no right or
# wrong ways, providing you get the data you require.

# Part 1 - List files in the Step_1 directory using glob.glob: https://docs.python.org/2/library/glob.html

import glob
import os

# List all Python files in current directory
print(glob.glob("*.py"))
# Change to parent of current directory (dangerous as you might struggle to change it back later...)
os.chdir("../")
print(glob.glob("*")) # no pattern match, lists all folders and files
# If you changed directory, you may need to change it back:

# Part 2 - List files using os (more painful)
os.chdir("Class_07")
all = os.listdir(os.curdir)# files and directories
print(all)
files = list(filter(os.path.isfile, os.listdir(os.curdir)))  # files only, might not find anything
print(files)

for file in os.listdir(os.curdir):
    if file.endswith(".shp"):
        print(file)

# Part 3 - List files using arcpy, note: all will return None
import arcpy

# ListFiles ({wild_card}) https://pro.arcgis.com/en/pro-app/arcpy/functions/listfiles.htm
print(arcpy.ListFiles("*"))

# ListDatasets ({wild_card}, {feature_type}) https://pro.arcgis.com/en/pro-app/arcpy/functions/listdatasets.htm
print(arcpy.ListDatasets("*",  "Feature"))
# ListFeatureClasses ({wild_card}, {feature_type}, {feature_dataset}) https://pro.arcgis.com/en/pro-app/arcpy/functions/listfeatureclasses.htm
print(arcpy.arcpy.ListFeatureClasses("*"))

# ListRasters ({wild_card}, {raster_type})  https://pro.arcgis.com/en/pro-app/arcpy/functions/listrasters.htm
print(arcpy.ListRasters("*", "TIF"))


# Tasks
# 1 - Using the supplied data in Step_1.zip (extract to a folder named Step_1), do the following:
# Hint, you should change your directory to Step_1
import arcpy
os.chdir(r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Class_07\Step_1")
arcpy.env.workspace = r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Class_07\Step_1"

# a - List and count all shapefiles, how many are there?
shape_files = arcpy.arcpy.ListFiles("*.shp")
print(len(arcpy.ListFiles("*.shp")))

# b - List and count all csv, how many are there?
shape_files = arcpy.arcpy.ListFiles("*.shp")
print(len(arcpy.ListFiles("*.shp")))

# c - List and count all folders, how many are there?
list_all_folders = os.listdir(os.curdir)
list_all_folders = [x for x in list_all_folders if os.path.isdir(x)]
print(list_all_folders)
print(len(list_all_folders))

# d - List and count all rasters in GRID format, how many are there?
rasters_grid = arcpy.ListRasters("*", "GRID")
print(rasters_grid)
print(len(rasters_grid))

# e - List and count all rasters in TIF format, how many are there?
rasters_tif = arcpy.ListRasters("*", "TIF")
print(rasters_tif)
print(len(rasters_tif))

# f - List and count all folders beginning with the letter/character S_, how many are there?
list_s_folders = os.listdir(os.curdir)
list_s_folders = [x for x in list_s_folders if "S_" in x]
print(list_s_folders)
print(len(list_s_folders))

#####
# Step 2 - Python Script from Tools
#####

# Perhaps one of the most common ways of constructing a Python script, particularly when using
# unfamiliar tools, is to run the tool and to extract the Python code from the "History" window
# once the tool has successfully run.

# In this example, we will process a directory of Landsat 8 images, by first running the tools
# that we need in ArcGIS Pro and Toolbox, we will then extract the Python code from each tool and
# build a Python script around it.

# Task 1 - Using Step_2_data.zip, select the first layer, and execute the tool "Composite Bands" on Winter_2013.
# you will need to composite all the band images (ending in Bn.tif (where n = band number), do not add the BQA.tif
# file. See Landsat 8 band reference -
# https://www.usgs.gov/faqs/what-are-best-landsat-spectral-bands-use-my-research?qt-news_science_products=0#qt-news_science_products

# Once the tool has successfully completed, go into the Geoprocessing "History" window, right click on the
# Completed tool, select "Copy as Python Snippet" and paste the tool output below:

# arcpy.management.CompositeBands(
#     in_rasters=r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Class_06\Step_2_data\Winter_2013\LC08_L1TP_012031_20131212_20170307_01_T1_B1.tif;"
#                r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Class_06\Step_2_data\Winter_2013\LC08_L1TP_012031_20131212_20170307_01_T1_B2.tif;"
#                r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Class_06\Step_2_data\Winter_2013\LC08_L1TP_012031_20131212_20170307_01_T1_B3.tif;"
#                r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Class_06\Step_2_data\Winter_2013\LC08_L1TP_012031_20131212_20170307_01_T1_B4.tif;"
#                r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Class_06\Step_2_data\Winter_2013\LC08_L1TP_012031_20131212_20170307_01_T1_B5.tif;"
#                r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Class_06\Step_2_data\Winter_2013\LC08_L1TP_012031_20131212_20170307_01_T1_B6.tif;"
#                r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Class_06\Step_2_data\Winter_2013\LC08_L1TP_012031_20131212_20170307_01_T1_B7.tif;"
#                r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Class_06\Step_2_data\Winter_2013\LC08_L1TP_012031_20131212_20170307_01_T1_B8.tif;"
#                r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Class_06\Step_2_data\Winter_2013\LC08_L1TP_012031_20131212_20170307_01_T1_B9.tif;"
#                r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Class_06\Step_2_data\Winter_2013\LC08_L1TP_012031_20131212_20170307_01_T1_B10.tif;"
#                r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Class_06\Step_2_data\Winter_2013\LC08_L1TP_012031_20131212_20170307_01_T1_B11.tif",
#     out_raster=r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Class_06\Step_2_data\winter_2013.tif"
# )


# Task 2 -  Now it is relatively easy to copy this and change the file name in order to run it on the Winter_2013 data
# but we are not going to do that, instead, we are going to use Python to do this for us from a directory name. Below,
# complete the code that I have provided.

# import arcpy, os
#
# base_path_directory = r'C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Class_06\Step_2_data\Winter_2013'
# arcpy.env.workspace = base_path_directory
#
# listofbands = arcpy.ListRasters()
# print(listofbands)
#
# listRasters = arcpy.ListRasters("*", "TIF")
# print(listRasters)
#
# # Remove the BQA.tif file from the list.
# listRasters = [x for x in listRasters if "BQA" not in x]
# print(listRasters)
#
# # We need to solve problem of sorting B1-B11 correctly
# noExtensionlistRasters = [os.path.splitext(x)[0] for x in listRasters]  # Removes file extension (tif) from each name
# print(noExtensionlistRasters)
# sorted_listRasters = sorted(noExtensionlistRasters, key=lambda x: int(
#     x[42:]))  # 42 characters in name before hit band number LC08_L1TP_012031_20131212_20170307_01_T1_B1
# sorted_listRasters = [x + ".tif" for x in sorted_listRasters]
# print(sorted_listRasters)
# arcpy.management.CompositeBands(listRasters,
#                                 r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Class_06\Step_2_data\Winter_2013_Composite.tif")

# Now edit the arcpy.CompositeBands_Management tool to run the Winter 2014 data, hint, you can provide the in_rasters
# argument as a list.


# Task 3 - This is difficult, now I want you to batch run the Composite Bands script on all of our Winter_201n
# data. Hint: use the list and starter code I have provided, and consider using a for loop to run through each year of data
# complete the composite bands tool for each one, and go from there.

import os, arcpy

listYears = ["2013", "2014", "2015", "2016", "2017", "2018", "2019"]

base_path_directory = r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Class_06\Step_2_data"
arcpy.env.workspace = base_path_directory


for year in listYears:
    arcpy.env.workspace = os.path.join(base_path_directory, "Winter_" + year)
    listofbands = arcpy.ListRasters()
    listofbands = listofbands[:-1] #remove last item in list
    b10name = listofbands[1]
    print(listofbands)
    listofbands.pop(1)

    listofbands = listofbands.append(b10name)
    print(listofbands)


# Consider what you want to do before you start. 1) for loop through listYears, 2) set your workspace to the correct
# year, 3) arcpy.ListRasters, 4) remove BQA.tif, 5) composite bands into a known location.


# Task 4 - See Step_2.py for the Task!

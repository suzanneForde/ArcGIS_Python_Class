
# Coding Challenege #8
# Convert some of your earlier code into a function.
# Rules are:
# 1) You must do more than one thing to your input to the function
# 2) the function must take two arguments or more
# 3) provide a zip file of example data within your repo


# Using Coding Challenge 4

import os
import arcpy

def intersect_analysis(target_feature_path, join_feature_path, output_feature_path):
    try:
        # check if output feature class already exists, delete if it does
        if arcpy.Exists(output_feature_path):
            arcpy.Delete_management(output_feature_path)

        # overlay the input feature classes
        arcpy.Intersect_analysis([target_feature_path, join_feature_path], output_feature_path)

        print("Intersect analysis completed successfully.")

    # return GIS messages
    except arcpy.ExecuteError:
        print(arcpy.GetMessages(2))

    except Exception as e:
        print(e)

# workspace
workspace = arcpy.env.workspace = r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Code_Chall\Chall_8_SForde\Data_from_chall04"
arcpy.env.overwriteOutput = True

target_feature = "Public_Water_Reservoirs.shp"
join_feature = "RIDOT_Roads__2016_.shp"
output_feature = "water_roads_join.shp"

intersect_analysis(target_feature, join_feature, output_feature)
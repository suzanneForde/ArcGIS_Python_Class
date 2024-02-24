
# Coding Challenge 4
# For this coding challenge, I want you to find a particular tool that you like in arcpy.
# It could be a tool that you have used in GIS before or something new.
# Try browsing the full tool list to get some insight here (click Tool Reference on the menu list to the left).
#
# Set up the tool to run in Python, add some useful comments, and importantly,
# provide some example data in your repository (try to make it open source, such as Open Streetmap, or RI GIS.
# You can add it as a zip file to your repository.
#
# My only requirements are:
#
# Comment your code well.
# Ensure that the code will run on my machine with only a single change to a single variable (i.e. a base folder location).


import arcpy
import os

# base folder path
script_dir = os.path.dirname(os.path.abspath(__file__))
workspace = os.path.join(script_dir, "workspace_04")

# target and join feature paths
target_feature = os.path.join(workspace, "RIPTA_Bus_Stops.shp")
join_feature = os.path.join(workspace, "RIDOT_Roads__2016_.shp")

# output feature class
output_feature = os.path.join(workspace, "bus_roads_join.shp")

# check if  output feature class already exists, delete if it does, this allows us to run the code more than once
try:
    if arcpy.Exists(output_feature):
        arcpy.Delete_management(output_feature)

# overlay the input feature classes
    arcpy.Intersect_analysis([target_feature, join_feature], output_feature)

    print("Intersect analysis completed successfully.")

# return GIS messages
except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))

except Exception as e:
    print(e)



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

workspace = r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Code_Chall\Chall_4_SForde\workspace_04"
arcpy.env.workspace = workspace

target_feature = os.path.join(workspace, r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Code_Chall\Chall_4_SForde\workspace_04\RIPTA_Bus_Stops.shp")
join_feature = os.path.join(workspace, r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Code_Chall\Chall_4_SForde\workspace_04\FACILITY_Schools_pk12_2023.shp")

# path to the output feature class
output_feature = os.path.join(workspace, r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Code_Chall\Chall_4_SForde\workspace_04\bus_school_join.shp")

try:
    # check if the output feature class already exists, delete if it does
    if arcpy.Exists(output_feature):
        arcpy.Delete_management(output_feature)

    # overlay the input feature classes
    arcpy.Intersect_analysis([target_feature, join_feature], output_feature)

    print("Intersect analysis completed successfully.")

except arcpy.ExecuteError:
    print(arcpy.GetMessages(2)) #returns GIS messages

except Exception as e:
    print(e)

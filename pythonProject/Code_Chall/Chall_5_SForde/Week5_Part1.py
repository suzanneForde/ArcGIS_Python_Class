#
#
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



import arcpy
arcpy.env.workspace = r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Class_05"

arcpy.env.overwriteOutput = True

in_Table = r"Step_1_Deep_Coral.csv"
x_coords = "decimalLongitude"
y_coords = "decimalLatitude"
z_coords = ""
out_Layer = "deepcoral"
saved_Layer = r"Step_1_Deep_Coral_Output.shp"

spRef = arcpy.SpatialReference(4326)  # 4326 == WGS 1984

lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)
#
# ##### 2. Print the count of the number of records in the file. (Hint: see above!)
# # https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/get-count.htm
#
print(arcpy.GetCount_management(out_Layer))
#
# ##### 3. Check the correct coordinate system has been applied (Hint: see last week!)
#
arcpy.CopyFeatures_management(lyr, saved_Layer)
#
if arcpy.Exists(saved_Layer):
    print("Created file successfully!")

desc = arcpy.Describe(saved_Layer)
print(desc.spatialReference.name)

##### 4. Visualize the file in ArcPro by dragging it into the program.
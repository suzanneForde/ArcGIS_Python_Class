#####
# Step 3 - Executing multiple tools - and automating most of it
#####

# We will use the exact same approach to generate a heatmap from a CSV file, but this time
# You will have to automate the extraction of start extent, opposite corner etc for the fishnet
# generation. I have given hints, but everything you are using here has been shown in last week's
# and this week's session.

# Using Step_3_Cepphus_grylle.csv:

# 1. Convert Step_3_Cepphus_grylle.csv to a shapefile.

import arcpy
arcpy.env.workspace = r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Class_05\Step_3_Cepphus_grylle"

arcpy.env.overwriteOutput = True

in_Table = r"Step_3_Cepphus_grylle.csv"
x_coords = "lon"
y_coords = "lat"
z_coords = " "
out_Layer = "cepphus"
saved_Layer = r"Step3_CG_Output.shp"

spRef = arcpy.SpatialReference(4326)  # 4326 == WGS 1984

lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, "")

print(arcpy.GetCount_management(out_Layer))

arcpy.CopyFeatures_management(lyr, saved_Layer)
if arcpy.Exists(saved_Layer):
    print("Created file successfully!")


# 2. Extact the Extent, i.e. XMin, XMax, YMin, YMax of the generated Cepphus_grylle shapefile.

desc = arcpy.Describe(saved_Layer)
XMin = desc.extent.XMin
XMax = desc.extent.XMax
YMin = desc.extent.YMin
YMax = desc.extent.YMax


# Set the origin of the fishnet

arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)

outFeatureClass = "Step_3_Fishnet.shp"

# 3. Generate a fishnet, but this time define the originCoordinate, yAxisCoordinate and oppositeCorner
# using the extracted extent from above. Hint: Formatting of the coordinate is important when generating
# the Fishnet, you must present it as: "-176.87 -41", note the space inbetween, and the fact that the
# entire thing is a string. Hint use: cellSizes of 0.25 degrees.

originCoordinate =  str(XMin) + " " + str(YMin)
yAxisCoordinate =  str(XMin) + " "  + str(YMin +1)
cellSizeWidth = "0.25"
cellSizeHeight = "0.25"
numRows = ""  # Leave blank, as we have set cellSize
numColumns = ""  # Leave blank, as we have set cellSize
oppositeCorner = str(XMax) + " " + str(YMax)
labels = "NO_LABELS"
templateExtent = "#"  # No need to use, as we have set yAxisCoordinate and oppositeCorner
geometryType = "POLYGON"  # Create a polygon, could be POLYLINE

arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
                               cellSizeWidth, cellSizeHeight, numRows, numColumns,
                               oppositeCorner, labels, templateExtent, geometryType)

if arcpy.Exists(outFeatureClass):
    print("Created Fishnet file successfully.")

# 4. Undertake a Spatial Join to join the fishnet to the observed points.


# 5. Check that the heatmap is created and delete the intermediate files (e.g. species shapefile and fishnet). Hint:
# arcpy.Delete_management()..

# 6. Visualize in ArcGIS Pro

# Hint: To stop your script failing due to unable to overwriteOutput error, use the overwriteOutput environment setting:
# import arcpy
# arcpy.env.overwriteOutput = True  # If you get "already exists error" even when True, ensure file is not open in
# # ArcGIS Pro or an other program such as Excel.


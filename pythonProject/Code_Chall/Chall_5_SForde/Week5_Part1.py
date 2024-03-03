
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
###############################################################

# NOTE: I converted xml to .csv in the Week5_FileConversion.py file. I learned a lot, but it was hell.
# For this challenge I chose to use Alaskan polar bear maternal dens data and sea otter females with pups data (Prince William Sound, Alaska)
# I figured since polar bears are predators to sea otters that looking at their proximity on a map would be interesting.

# CREATING SHAPEFILES

import arcpy
# set workspace:
workspace_dir = r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Code_Chall\Chall_5_SForde\Species_Data"
arcpy.env.workspace = workspace_dir
arcpy.env.overwriteOutput = True

# Merges .csv data column names set to (x,y) values for map
in_Table = r"merged_species_file.csv"
x_coords = "decimalLongitude"
y_coords = "decimalLatitude"
z_coords = ""
out_Layer = "bear_den_otter_pups"
saved_Layer = r"merged_species_output.shp"

# setting spatial reference
spRef = arcpy.SpatialReference(4326)  # 4326 == WGS 1984

lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)

print(arcpy.GetCount_management(out_Layer))

# extracting extent values
arcpy.CopyFeatures_management(lyr, saved_Layer) # Save to a layer file
desc = arcpy.Describe(saved_Layer)
XMin = desc.extent.XMin
XMax = desc.extent.XMax
YMin = desc.extent.YMin
YMax = desc.extent.YMax
print("Extent:", XMin, XMax, YMin, YMax)

if arcpy.Exists(saved_Layer):
    print("Merged species shapefile created successfully!")

arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)

outFeatureClass = "Species_Fishnet.shp"  # output fishnet

# Origin of the fishnet
originCoordinate = str(XMin) + " " + str(YMin)
yAxisCoordinate = str(XMin) + " " + str(YMin + 1)
cellSizeWidth = "5" # I set cell size to 5, but I am still a bit confused on what factors I could even make that decision on? I chose 5 just because.
cellSizeHeight = "5"
numRows = ""  # Leave blank, as we have set cellSize
numColumns = "" # Leave blank, as we have set cellSize
oppositeCorner = str(XMax) + " " + str(YMax)  # i.e. max x and max y coordinate
labels = "NO_LABELS"
templateExtent = "#"  # No need to use, as we have set yAxisCoordinate and oppositeCorner
geometryType = "POLYGON"  # Create a polygon, could be POLYLINE

arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
                               cellSizeWidth, cellSizeHeight, "", "",
                               str(XMax) + " " + str(YMax), "NO_LABELS",
                               "#", "POLYGON")

print("Fishnet grid created successfully!")


# Spatial Join to join the fishnet to observed points.
target_features = "Species_Fishnet.shp"  # fishnet grid
join_features = "merged_species_output.shp"  # point data
out_feature_class = "species_heatmap.shp"  # output heatmap

# Perform spatial join
arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                           join_operation="JOIN_ONE_TO_ONE",
                           join_type="KEEP_ALL",
                           match_option="INTERSECT",
                           search_radius="",
                           distance_field_name="")
print("Polar bear den and otter moms and pups heatmap created successfully!")

# if arcpy.Exists(out_feature_class):
#     print("Created Heatmap file successfully!")
#     print("Deleting intermediate files")
#     # arcpy.Delete_management(target_features)
#     # arcpy.Delete_management(join_features)
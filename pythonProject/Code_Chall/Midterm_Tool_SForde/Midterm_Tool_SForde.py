
# For this midterm tool, I originally decided to conduct a proximity analysis of libraries near 100 feet of schools in Providence.
# However, this was too challenging because it seemed the data files I downloaded from RIGIS were corrupted.
# Points for schools would not show up on ArcGIS even though the shapefiles contained data (in the attribute tables)
# Instead I conducted a proximity analysis of bus stops within 1 mile of libraries.
# This information could be used to create a bus guide for local residents in need of books or other materials.



import arcpy
import os

# Setting up the workspace and file paths
arcpy.env.workspace = r'C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Code_Chall\Midterm_Tool_SForde\Library_BusStops_Data'

# setting coordinate system
factory_code = 4326  # == WGS 1984
coordinate_system = arcpy.SpatialReference(factory_code)

# Paths to provided data files
BusStop_shapefile = "RIPTA_Bus_Stops.shp"
Library_shapefile = "Libraries.shp"
state_boundary_shapefile = "Municipalities_(1997).shp"

# defining projection for each dataset
arcpy.management.DefineProjection(BusStop_shapefile, coordinate_system)
arcpy.management.DefineProjection(Library_shapefile, coordinate_system)
arcpy.management.DefineProjection(state_boundary_shapefile, coordinate_system)

# Setting the extent
extent = arcpy.Describe(state_boundary_shapefile).extent
arcpy.env.extent = extent

# Output folder paths for results
output_folder = "output_data"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)  # create folder if it doesn't exist
else:
    print("Output folder already exists.")

# Checking attribute table for the Rhode Island shapefile.
fields = arcpy.ListFields(state_boundary_shapefile)

if fields:
    print("Attribute table exists for the shapefile.")

    # Access the fields in the attribute table
    print("Field names and types:")
    for field in fields:
        print(f"{field.name}: {field.type}")

    # Access other attribute table properties using Describe
    desc = arcpy.Describe(state_boundary_shapefile)
    print("Shape type:", desc.shapeType)
    print("Spatial reference:", desc.spatialReference.name)

else:
    print("Attribute table does not exist for the shapefile.")


providence_boundary = os.path.join(output_folder, "Providence_boundary.shp")
libraries_buffered = os.path.join(output_folder, "Libraries_buffered.shp")
bus_stops_in_buffer = os.path.join(output_folder, "Bus_Stops_in_Buffer.shp")

# if output file already exists, delete
output_files = [providence_boundary, libraries_buffered, bus_stops_in_buffer]

for file in output_files:
    if arcpy.Exists(file):
        arcpy.Delete_management(file)
        print(f"{file} already exists. Deleting the existing file...")

print("Step 1: Creating Providence boundary...")
# Create a feature layer only once
arcpy.MakeFeatureLayer_management(state_boundary_shapefile, "state_boundary_layer")

# Selecting features with the desired attribute
arcpy.SelectLayerByAttribute_management("state_boundary_layer", "NEW_SELECTION", "NAME = 'Providence'")

# Creating a new feature class with the selected features
arcpy.FeatureClassToFeatureClass_conversion("state_boundary_layer", output_folder, "Providence_boundary.shp")
print("Providence boundary created successfully.")

print("Step 2: Buffering libraries...")
# buffering libraries
arcpy.Buffer_analysis(Library_shapefile, libraries_buffered, "1320 feet")
print("Libraries buffered successfully.")

print("Step 3: Selecting bus stops within 1320 feet of buffered libraries...")
# Selecting bus stops within 1320 feet of buffered libraries
arcpy.MakeFeatureLayer_management(BusStop_shapefile, "bus_stops_layer")
arcpy.SelectLayerByLocation_management("bus_stops_layer", "WITHIN_A_DISTANCE", libraries_buffered, "1320 feet")
arcpy.CopyFeatures_management("bus_stops_layer", bus_stops_in_buffer)
print("Bus stops within 1320 feet of buffered libraries selected successfully.")

print("Process completed successfully.")
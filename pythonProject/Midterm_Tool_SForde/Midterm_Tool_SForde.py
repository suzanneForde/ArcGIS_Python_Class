
# For this midterm tool, I originally decided to conduct a proximity analysis of libraries near 100 feet of schools in Providence.
# However, this was too challenging because it seemed the data files I downloaded from RIGIS were corrupted.
# Points for schools would not show up on ArcGIS even though the shapefiles contained data (in the attribute tables)
# Instead I conducted a proximity analysis of bus stops within 1,320 feet of libraries.
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

# Checking attribute table for the Rhode Island shapefile because I was having trouble creating a shapefile output for Providence.
# The data existed but would not display in ArcGIS
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
arcpy.SelectLayerByAttribute_management("state_boundary_layer", "NEW_SELECTION", "UPPER(NAME) = 'PROVIDENCE'")

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

print("Step 4: Selecting libraries and bus stops within Providence boundary...")

# Creating Providence boundary feature layer
arcpy.MakeFeatureLayer_management(providence_boundary, "providence_boundary_layer")

# Creating feature layers for buffered libraries and bus stops
arcpy.MakeFeatureLayer_management(libraries_buffered, "libraries_buffered_layer")
arcpy.MakeFeatureLayer_management(bus_stops_in_buffer, "bus_stops_in_buffer_layer")

# Selecting features within Providence boundary
arcpy.SelectLayerByLocation_management("libraries_buffered_layer", "COMPLETELY_WITHIN", "providence_boundary_layer")
arcpy.SelectLayerByLocation_management("bus_stops_in_buffer_layer", "COMPLETELY_WITHIN", "providence_boundary_layer")

# Copying selected features to new shapefiles
providence_libraries = os.path.join(output_folder, "Providence_libraries.shp")
providence_bus_stops = os.path.join(output_folder, "Providence_bus_stops.shp")

# Delete existing output files if they exist
if arcpy.Exists(providence_libraries):
    arcpy.Delete_management(providence_libraries)
if arcpy.Exists(providence_bus_stops):
    arcpy.Delete_management(providence_bus_stops)

# Copy features to new shapefiles
arcpy.CopyFeatures_management("libraries_buffered_layer", providence_libraries)
arcpy.CopyFeatures_management("bus_stops_in_buffer_layer", providence_bus_stops)

print("Features within Providence boundary selected successfully.")

print("Final features for map creation are: Providence_boundary.shp, Providence_libraries.shp, and Providence_bus_stops.shp")

print("The following bus stop numbers are those that are within 1320 feet of Providence libraries.")

# Get bus stop numbers (Route) within the buffer
bus_stop_numbers = set()  # Using a set to store unique bus stop numbers
with arcpy.da.SearchCursor(providence_bus_stops, ["ROUTE"]) as cursor:
    for row in cursor:
        bus_stop_numbers.add(row[0])

# Print unique bus stop numbers
for bus_stop_number in bus_stop_numbers:
    print(bus_stop_number)

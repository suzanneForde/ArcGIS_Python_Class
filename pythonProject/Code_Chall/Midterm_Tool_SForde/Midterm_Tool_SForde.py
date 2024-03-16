
# For this midterm tool, I decided to conduct a proximity analysis of libraries near 100 feet of schools in Providence.
#



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

providence_boundary = os.path.join(output_folder, "Providence_boundary.shp")
schools_in_providence = os.path.join(output_folder, "Stops_in_Providence.shp")
schools_buffered = os.path.join(output_folder, "Stops_buffered.shp")
schools_library_intersections = os.path.join(output_folder, "Stops_libraries_intersections.shp")

# if output file already exists, delete
output_files = [providence_boundary, schools_in_providence, schools_buffered, schools_library_intersections]

for file in output_files:
    if arcpy.Exists(file):
        arcpy.Delete_management(file)
        print(f"{file} already exists. Deleting the existing file...")


print("Step 1: Creating Providence boundary...")
# creating a feature layer from state boundary shapefile
arcpy.MakeFeatureLayer_management(state_boundary_shapefile, "state_boundary_layer")

# selecting Providence from the state boundary
arcpy.SelectLayerByAttribute_management("state_boundary_layer", "NEW_SELECTION", "NAME = 'Providence'")

# copying the selected features to create the Providence boundary shapefile
arcpy.CopyFeatures_management("state_boundary_layer", providence_boundary)
print("Providence boundary created successfully.")

print("Step 2: Extracting data within Providence boundary...")
# extracting data within Providence boundary
arcpy.MakeFeatureLayer_management(BusStop_shapefile, "stops_layer")
arcpy.MakeFeatureLayer_management(providence_boundary, "providence_layer")
arcpy.SelectLayerByLocation_management("stops_layer", "INTERSECT", "providence_layer")
arcpy.CopyFeatures_management("stops_layer", schools_in_providence)
print("Data extracted within Providence boundary successfully.")

print("Step 3: Buffering bus stops within Providence...")
# buffering schools
arcpy.Buffer_analysis(schools_in_providence, schools_buffered, "20 feet")
print("Bus stops buffered successfully.")

print("Step 4: Performing intersection with libraries...")
# intersecting buffered schools with libraries
arcpy.Intersect_analysis([schools_buffered, Library_shapefile], schools_library_intersections)
print("Intersection with libraries completed successfully.")


print("Process completed successfully.")


# For this midterm tool, I decided to conduct a proximity analysis of libraries near 100 feet of schools in Providence.
# 



import arcpy
import os

# Setting up the workspace and file paths
arcpy.env.workspace = r'C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Code_Chall\Midterm_Tool_SForde\School_Library_Data'

# Paths to provided data files
School_shapefile = "FACILITY_Schools_pk12_2023.shp"
Library_shapefile = "FACILITY_Public_Libraries_2021.shp"
state_boundary_shapefile = "Municipalities_(1997).shp"

# Output folder paths for results
output_folder = "output_data"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)  # create folder if it doesn't exist
else:
    print("Output folder already exists.")

providence_boundary = os.path.join(output_folder, "Providence_boundary.shp")
schools_in_providence = os.path.join(output_folder, "Schools_in_Providence.shp")
schools_buffered = os.path.join(output_folder, "Schools_buffered.shp")
schools_library_intersections = os.path.join(output_folder, "Schools_libraries_intersections.shp")

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
arcpy.MakeFeatureLayer_management(School_shapefile, "schools_layer")
arcpy.MakeFeatureLayer_management(providence_boundary, "providence_layer")
arcpy.SelectLayerByLocation_management("schools_layer", "INTERSECT", "providence_layer")
arcpy.CopyFeatures_management("schools_layer", schools_in_providence)
print("Data extracted within Providence boundary successfully.")

print("Step 3: Buffering schools within Providence...")
# buffering schools
arcpy.Buffer_analysis(schools_in_providence, schools_buffered, "100 Meters")
print("Schools buffered successfully.")

print("Step 4: Performing intersection with libraries...")
# intersecting buffered schools with libraries
arcpy.Intersect_analysis([schools_buffered, Library_shapefile], schools_library_intersections)
print("Intersection with libraries completed successfully.")

arcpy.Delete_management("schools_layer")
arcpy.Delete_management("providence_layer")
arcpy.Delete_management("state_boundary_layer")

print("Process completed successfully.")

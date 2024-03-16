

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
os.makedirs(output_folder) # creating the folder if it doesn't exist
providence_boundary = os.path.join(output_folder, "Providence_boundary.shp")
schools_in_providence = os.path.join(output_folder, "Schools_in_Providence.shp")
schools_buffered = os.path.join(output_folder, "Schools_buffered.shp")
schools_library_intersections = os.path.join(output_folder, "Schools_libraries_intersections.shp")

# creating a feature layer from state boundary shapefile
arcpy.MakeFeatureLayer_management(state_boundary_shapefile, "state_boundary_layer")

# selecting Providence from the state boundary
arcpy.SelectLayerByAttribute_management("state_boundary_layer", "NEW_SELECTION", "NAME = 'Providence'")

# copying the selected features to create the Providence boundary shapefile
arcpy.CopyFeatures_management("state_boundary_layer", providence_boundary)

# extracting data within Providence boundary
arcpy.MakeFeatureLayer_management()





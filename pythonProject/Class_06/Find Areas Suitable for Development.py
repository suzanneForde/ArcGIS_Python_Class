
import arcpy
import os

arcpy.env.overwriteOutput = False

base_path_directory = r'C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Class_06\Step_1_data\Step_1_data'
arcpy.env.workspace = base_path_directory

# inputs for script
Roads = os.path.join(base_path_directory, "RI_Roads.shp")
Places = os.path.join(base_path_directory, "Places.shp")
State_Boundary = os.path.join(base_path_directory, "State_Boundary_1997.shp")

# Make temporary file folder
if not os.path.exists(os.path.join(base_path_directory, "temporary_files")):
        os.mkdir(os.path.join(base_path_directory, "temporary_files"))

# Process: Buffer places (Buffer) (analysis)
if not os.path.exists(os.path.join(base_path_directory, "temporary_files", "RI_Roads_Buffer")):
    arcpy.analysis.Buffer(in_features=Roads,
                          out_feature_class=os.path.join(base_path_directory, "temporary_files", "Places_Buffer.shp"),
                          buffer_distance_or_field="10 Miles",
                          dissolve_option="ALL")
    print("Place Buffered Successfully.")
else:
    print("Places buffered already there.")


# Process: Buffered data intersected (Intersect) (Analysis)
if not os.path.exists(os.path.join(base_path_directory, "temporary_files", "RI_Roads_Buffer_Intersect.shp")):
    buffered_roads=os.path.join(base_path_directory, "temporary_files", "RI_Roads_Buffer.shp"),
    buffered_places=os.path.join(base_path_directory, "temporary_files", 'Places_Buffer.shp')
    arcpy.analysis.Intersect(in_features=[[buffered_roads, ""], [buffered_places, ""]]),
    out_feature_class=os.path.join(base_path_directory, "temporary_files", "Intersected.shp")
    print("Buffered data successfully.")
else:
    print("Data already intersected")

# # Process: Clip (Clip) (analysis)
if not os.path.exists(os.path.join(base_path_directory, "temporary_files", "Suitable_areas_for_development.shp")):
    arcpy.analysis.Clip(in_features=os.path.join(base_path_directory), "temporary_files", "Intersected.shp"),
    clip_features)=State_Boundary,
    out_feature_class=os.path.join(base_path_directory, "temporary_files", "Suitable_areas_for_development.shp"))
    print("Data clipped successfully.")
else:
    print("Data already clipped.")

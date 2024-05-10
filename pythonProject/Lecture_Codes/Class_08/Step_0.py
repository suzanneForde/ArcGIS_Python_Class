# Step 0 - Warm up task

# Develop a small script that uses two datasets from RIGIS.org and undertake a geoprocessing routine on the
# data.

# This could be a spatial join, a buffer, an intersect, an extract by mask for example.
# there are no restrictions on the tool or dataset, and there is no answer file for this,
# so please do go forward with producing a simple script.

import os
import arcpy

workspace = arcpy.env.workspace = r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Class_08\Step_0_data"
arcpy.env.overwriteOutput = True

# Defining input datasets
groundwater_reservoirs = os.path.join(workspace, "Groundwater_Reservoirs.shp")
sanitary_waste = os.path.join(workspace, "RIPDES_Sanitary_Waste_Sites.shp")

# Define output feature classes
buffered_groundwater_reservoirs = os.path.join(workspace, "buffered_groundwater_reservoirs.shp")
buffered_sanitary_waste = os.path.join(workspace, "buffered_sanitary_waste.shp")

# Buffer analysis
buffer_distance = "1000 meters"

try:
    # Buffer groundwater reservoirs
    arcpy.Buffer_analysis(groundwater_reservoirs, buffered_groundwater_reservoirs, buffer_distance)

    # Buffer sanitary waste
    arcpy.Buffer_analysis(sanitary_waste, buffered_sanitary_waste, buffer_distance)

    print("Buffer analysis completed successfully.")

except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))

except Exception as e:
    print(e)



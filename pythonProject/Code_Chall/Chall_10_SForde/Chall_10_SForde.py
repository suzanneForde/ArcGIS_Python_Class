###
# Coding Challenge 10
###

# Task 1 - Use what you have learned to process the Landsat files provided, this time, you know you are interested in
# the NVDI index which will use Bands 4 (red, aka vis) and 5 (near-infrared, aka nir) from the Landsat 8 imagery,
# Data provided are monthly (a couple are missing due to cloud coverage) during the year 2015 for the State of RI,
# and stored in the file Landsat_data_lfs.zip.
#
# Before you start, here is a suggested workflow:
#
# Extract the Landsat_data_lfs.zip file into a known location.
# For each month provided, you want to calculate the NVDI, using the equation: nvdi = (nir - vis) / (nir + vis)
# https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index.
# Consider using the Raster Calculator Tool in ArcMap and using "Copy as Python Snippet" for the first calculation.

# The only rule is, you should run your script once, and generate the NVDI for ALL MONTHS provided.
# As part of your code submission, you should also provide a visualization document
# (e.g. an ArcMap layout in PDF format), showing the patterns for an area of RI that you find interesting.

import arcpy
arcpy.env.workspace = r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Code_Chall\Chall_10_SForde\Landsat_Data_Folder"

# List the landsat files
landsat_files = arcpy.ListRasters()

# looping through each Landsat file
for landsat_file in landsat_files:
    # Extract month from file name (assuming file names have format: Landsat_YYYY_MM)
    month = landsat_file.split("_")[1]

    # Extract NIR and VIS bands
    nir_band = arcpy.Raster(landsat_file + "\\Band5")
    vis_band = arcpy.Raster(landsat_file + "\\Band4")

    # Calculate NDVI
    ndvi = (nir_band - vis_band) / (nir_band + vis_band)

    # Save NDVI raster
    ndvi.save("NDVI_" + month)

    print("NDVI calculation completed for month:", month)

print("All NDVI calculations completed.")






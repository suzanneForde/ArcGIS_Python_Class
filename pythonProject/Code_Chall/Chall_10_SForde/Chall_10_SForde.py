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
import os

landsat_folder = r"C:\Users\Suzie\OneDrive\Desktop\Chall_10_Data\Landsat_Files"
arcpy.env.workspace = landsat_folder

# list of all folders in the Landsat folder
folder_list = [folder for folder in os.listdir(landsat_folder) if os.path.isdir(os.path.join(landsat_folder, folder))]

# loop through each folder
for folder in folder_list:
    # month from the folder name (last two characters)
    month = folder[-2:]

    # list of all TIFF files in folder
    tif_files = [file for file in os.listdir(os.path.join(landsat_folder, folder)) if file.endswith('.tif')]

    # variables to store NIR and VIS band paths
    nir_band_path = None
    vis_band_path = None

    # find NIR and VIS bands within current folder
    for file in tif_files:
        if file.endswith('_B5.tif'):  # NIR band
            nir_band_path = os.path.join(landsat_folder, folder, file)
        elif file.endswith('_B4.tif'):  # VIS band
            vis_band_path = os.path.join(landsat_folder, folder, file)

    # check if both NIR and VIS bands are found
    if nir_band_path and vis_band_path:
        # open NIR and VIS bands as rasters
        nir_band = arcpy.Raster(nir_band_path)
        vis_band = arcpy.Raster(vis_band_path)

        # calculate NDVI
        ndvi = (nir_band - vis_band) / (nir_band + vis_band)

        # define output NDVI raster path
        ndvi_output_path = os.path.join(landsat_folder, folder, "NDVI_" + month + ".tif")

        # save NDVI raster
        arcpy.CopyRaster_management(ndvi, ndvi_output_path, "", "", "", "NONE", "NONE", "")

        print("NDVI calculation completed for month:", month, "in folder:", folder)
        print("Output NDVI raster saved to:", ndvi_output_path)
    else:
        print("NIR or VIS band not found in folder:", folder)

print("All NDVI calculations completed.")



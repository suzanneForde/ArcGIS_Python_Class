
####
# Coding Challenge 9
####

# Objective: utilize arcpy.da module to undertake some basic partitioning of dataset.
# Work with the Forest Health Works dataset from RI GIS (provided as a downloadable ZIP file in this repository).
# Using the arcpy.da module, extract all sites that have a photo of the invasive species (Field: PHOTO)
# into a new Shapefile, and do some basic counts of the dataset.
# In summary, addressing the following:
# 1. Count how many individual records have photos, and how many do not (2 numbers), print the results.
# 2. Count how many unique species there are in the dataset, print the result.
# 3. Generate two shapefiles, one with photos and the other without.

import arcpy

arcpy.env.workspace = r"H:\NRS528_2024\Suzie_Forde\pythonProject\Code_Chall\Chall_9_SForde\RI_Forest_Data_Folder"
RI_Forest = "RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp"

output_with_photos = "RI_Forest_With_Photos.shp"
output_without_photos = "RI_Forest_Without_Photos.shp"

# Delete existing output shapefiles if they exist
if arcpy.Exists(output_with_photos):
    arcpy.management.Delete(output_with_photos)
if arcpy.Exists(output_without_photos):
    arcpy.management.Delete(output_without_photos)

# defining fields
photo_field = "PHOTO"
species_field = "Species"

# individual records with photos and without
count_with_photos = 0
count_without_photos = 0

# list to store unique species
unique_species = []

# iterating through input feature class
with arcpy.da.SearchCursor(RI_Forest, [photo_field, species_field]) as cursor:
    for row in cursor:
        if row[0]:
            count_with_photos += 1
        else:
            count_without_photos += 1

        if row[1] not in unique_species:
            unique_species.append(row[1])

# printing counts
print("Number of records with photos:", count_with_photos)
print("Number of records without photos:", count_without_photos)
print("Number of unique species:", len(unique_species))

# generating shapefiles
arcpy.Select_analysis(RI_Forest, output_with_photos, "{} = 'Y'".format(photo_field))
arcpy.Select_analysis(RI_Forest, output_without_photos,
                      "{} = 'N' OR {} IS NULL".format(photo_field, photo_field))

print("Shapefiles created successfully.")


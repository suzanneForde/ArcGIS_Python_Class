
#####
# Step 0 - Practice tasks before we start.
#####

# For each filename in the list_of_file_names, replace the . with _ and append a new file extension of ".shp"
# each filename should look like: "file1_csv.shp", print the output filename.

list_of_file_names = ["file1.csv", "file2.csv", "file3.csv", "file4.csv", "file5.csv"]

output_filenames = [filename.replace(".", "_") + ".shp" for filename in list_of_file_names]

print(output_filenames)

# How many files are in the list?
file_amnt = len(list_of_file_names)
print("Number of files in the list:", file_amnt)

# What is the first file name in the list_of_file_names?
first_filename = list_of_file_names[0]
print("First file name in the list:", first_filename)

# Write the following data to a csv file called species1.csv (hint, just write it to a file):
data = "scientificName,	decimalLongitude,	decimalLatitude\n" \
       "Desmophyllum pertusum,	-88.37752,	29.06926\n" \
       "Desmophyllum dianthus,	-119.4718,	33.91861"


with open("species1.csv", "w") as file:
       file.write(data)
       print("Data added to csv file")


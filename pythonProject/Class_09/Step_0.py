
#####
# Step 0 - Practice tasks before we start.
#####

# Express these items as a list using list append (i.e. .append) and print it:

item1 = "woodlands.shp"
item2 = "marshlands.shp"
item3 = "beaches.shp"

items_list = []

items_list.append(item1)
items_list.append(item2)
items_list.append(item3)
print(items_list)

# How many files are in the list?

print(len(items_list))

# Take this list of files (file_list), and using a for loop, go through each file name and change
# the file extension from shp to csv and print new_extension_file_list.
# Hint: I would use something like filename.split(".") to extract the filename[0] which would be the
# part of the name without the extension.

new_extension_file_list = []

for file in items_list:
    file_name = file.split(".")
    new_extension_file_list.append(file_name[0] + ".csv")

print(new_extension_file_list)

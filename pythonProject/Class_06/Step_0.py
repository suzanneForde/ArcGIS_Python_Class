
#####
# Step 0 - Practice tasks before we start.
#####

# Express this string of input files as a list, call the resulting list listFiles and print it:

stringFiles = "file1.asc;file2.asc;file3.asc;file4.asc;file5.asc"


# How many files are in the list?
listfiles = stringFiles.split(";")
print(listfiles)

print(len(listfiles))

# Take this list of files (listFiles), and using a for loop, go through each file name and print it.
for file in listfiles:
    print(file)

# Now, using the code below, create those files, and add a small piece of text ("this is my file") to each file:
for file in listfiles:
    file_create = open(file, "r")
    file_create.write("This is my file\n")
    print("Created: " + file)

# Now do the opposite, read the contents of each file and print it, here is some example code:
# file = open("testfile.txt", "r")
# file_contents = file.read()
# print (file_contents)
# file.close()



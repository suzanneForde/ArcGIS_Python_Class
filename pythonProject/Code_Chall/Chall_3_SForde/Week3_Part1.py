
###
# Part 1
###

import os


file_path0 = r"C:/TEST_FOLDER"
os.mkdir(file_path0)


## Creating subdirectories

file_path1 = r"C:/TEST_FOLDER/draft_code"
os.mkdir(file_path1)
#
file_path2 = r"C:/TEST_FOLDER/includes"
os.mkdir(file_path2)

file_path3 = r"C:/TEST_FOLDER/layouts"
os.mkdir(file_path3)

file_path4 = r"C:/TEST_FOLDER/sites"
os.mkdir(file_path4)


## Creating sub-sub directories

subfolder_names = ['pending', 'complete']
for subfolder_name in subfolder_names:
    os.makedirs(os.path.join(r"C:/TEST_FOLDER/draft_code", subfolder_name))


subfolder_names2 = ['default', 'post']
for subfolder_name in subfolder_names2:
    os.makedirs(os.path.join(r"C:/TEST_FOLDER/layouts", subfolder_name))


## Sub-sub-sub directories

subfolder_names3 = ['posted']
for subfolder_name in subfolder_names3:
    os.makedirs(os.path.join(r"C:/TEST_FOLDER/layouts/post", subfolder_name))


# Checking directory
list = os.listdir(file_path0)
print(list)

for folder_name in list:
    if folder_name == "TEST_CODE":
        print('name dir EXISTS')
    else:
        print('name dir NOT EXIST')

# Prints dir not exist 4 times?


# os.removedirs(TEST_FOLDER)


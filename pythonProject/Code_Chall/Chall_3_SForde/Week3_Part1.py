
###
# Part 1
###

import os


file_path1 = r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Code_Chall\Chall_3_SForde/draft_code"
os.mkdir(file_path1)

file_path2 = r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Code_Chall\Chall_3_SForde/includes"
os.mkdir(file_path2)

file_path3 = r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Code_Chall\Chall_3_SForde/layouts"
os.mkdir(file_path3)

file_path4 = r"C:\NRS528_Py_GIS\ArcGIS_Python_Class\pythonProject\Code_Chall\Chall_3_SForde/sites"
os.mkdir(file_path4)


subfolder_names = ['pending', 'complete']
for subfolder_name in subfolder_names:
    os.makedirs(os.path.join('draft_code', subfolder_name))


subfolder_names = ['pending', 'complete']
for subfolder_name in subfolder_names:
    os.makedirs(os.path.join('draft_code', subfolder_name))


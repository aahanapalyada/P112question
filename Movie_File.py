import os
import shutil

from_dir = "/Users/kiranpalyada/Desktop/Organize"
to_dir = "/Users/kiranpalyada/Desktop/Document_Files"

list_of_files = os.listdir(from_dir)

for files in list_of_files:
    root, ext = os.path.splitext(files)
    print(root,ext)

while ext == "":
    continue

if ext in ['.txt', '.doc', '.docx', '.pdf']:
    path1 = from_dir + '/' + files
    path2 = to_dir + '/' + "Document_Files"
    path3 = to_dir + '/' + "Document_Files" + '/' + files

if os.path.exists(path2):
    print("Moving" + files + "...")
    shutil.move(path1,path3)
else:
    os.makedirs(path2)
    print("Moving" + files + "...")
    shutil.move(path1,path3)  


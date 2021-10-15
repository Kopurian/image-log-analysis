import os
import shutil


source_path = r'D:\DTSData10-01-21'
folders = os.listdir(source_path)
dest_file = r'D:\Exported DTS CSV'
for folder in folders:
    folder_path = os.path.join(source_path, folder)
    files = os.listdir(folder_path)
    export_folder = os.path.join(dest_file, folder)
    if not os.path.exists(export_folder):
        os.mkdir(export_folder)
    for file in files:
        if file.endswith('.tra.temperature.csv'):
            file_path = os.path.join(folder_path, file)
            shutil.copy(file_path, export_folder)
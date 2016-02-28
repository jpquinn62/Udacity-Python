import os

def rename_files():
    # get file names from folder
    file_list = os.listdir(r"c:\project_files")
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is: " + saved_path)
    os.chdir(r"c:\project_files")
    # for each file, rename the file
    for file_name in file_list:
        print("Old Name - " + file_name)
        print("New Name - " + file_name.translate(None,"0123456789"))
        os.rename(file_name, file_name.translate(None,"0123456789"))
    os.chdir(saved_path)
rename_files()

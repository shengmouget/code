import os 
PATH_PATH = "./案例_files"
file_lists = os.listdir("案例_files")

for file_list in file_lists:
    ole_file = os.path.join(PATH_PATH,file_list)
    new_file = file_list.replace("-【三通it学院 www.santongit.com】","")
    new_file = os.path.join(PATH_PATH,new_file)
    os.renames(ole_file,new_file)
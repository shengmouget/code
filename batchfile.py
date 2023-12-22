import os 

# 获取需要修改的文件列表
def get_file_list(dir_path):
    return os.listdir(dir_path)

# 获取文件名
def get_file_name(file_path):
    return os.listdir(file_path)

# 旧文件地址
old_name_path = ""
file_list = get_file_list(old_name_path)
# 新文件地址
new_name_path = ""
name_list = get_file_name(new_name_path)

# 遍历文件列表
for file,name in zip(file_list,name_list):
    old_file_name = os.path.join(old_name_path,file)

    # 设置新文件名
    new_name = os.path.join(old_name_path,name)

    os.rename(old_file_name,new_name)
    print(file,"---->",name)



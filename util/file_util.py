import os
import sys

def get_images(file_dir):
    img_files = []
    img_suffix = ["jpg", "jpeg", "png", "JPG"]
    for img in os.listdir(file_dir):
        if img.split(".")[-1] in img_suffix:
            img_files.append(os.path.join(os.path.abspath(file_dir), img))
    return img_files

#生成资源文件目录访问路径
def resource_path(relative_path):
    if getattr(sys, 'frozen', False): #是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
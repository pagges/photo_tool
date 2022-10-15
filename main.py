from process.process_frame import *

if __name__ == '__main__':
    print("generate white picture frame automatically")
    # 待处理的图片文件夹
    images_path = input("Please enter the folder location of your photo :\n")
    # 处理后文件保存路径
    save_path = input("Please enter a file path to save the output photo :\n")
    process_frame(images_path, save_path)
    input("Enter enter end")

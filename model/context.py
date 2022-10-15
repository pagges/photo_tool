import os

import util.extract_exif_info
from .frame_config import FrameConfig


class Context(FrameConfig):
    # exif 信息
    exif_info = None
    # 图片的源文件路径
    source_image_file_path = ""
    # 文件保存的文件夹路径
    save_dir = ""

    def __init__(self, source_image_file_path, save_dir):
        print(source_image_file_path)
        if os.path.exists(source_image_file_path):
            self.source_image_file_path = source_image_file_path
            self.save_dir = save_dir
            self.exif_info = util.extract_exif_info.get_exif_info(self.source_image_file_path)
        else:
            self

    def get_exif(self):
        return self.exif_info

    def get_exif_msg(self):
        return self.exif_info.getExifMessage()

    def get_orientation(self):
        return self.exif_info.orientation

import os

from PIL import Image, ImageDraw, ImageFont
from util.file_util import *
from .base_action import *


class GenFrameAction(IAction):
    def __init__(self, context):
        self.context = context

    def accept(self):
        pass

    def do_action(self):
        # 读取图片
        origin_img = Image.open(self.context.source_image_file_path)
        origin_img = origin_img.rotate(self.context.get_orientation(), expand=True)
        width = origin_img.size[0]
        height = origin_img.size[1]

        # 添加边框
        frame_width = width + self.context.padding_width
        frame_height = height + self.context.padding_width
        # 底部空间预览出一条边框，填写参数信息
        final_height = frame_height + self.context.padding_width
        box = (int((frame_width - width) / 2), int((frame_height - height) / 2))
        img_new = Image.new(mode='RGB', size=(frame_width, final_height), color=self.context.padding_color)  # 创建一张新图
        img_new.paste(origin_img, box)

        # 相机信息文字尺寸
        camera_size = int(width / 60)
        camera_font = ImageFont.truetype(resource_path(os.path.join("assert", "Average.ttf")), camera_size,
                                         encoding="utf-8")
        # 参数文字属性
        param_size = int(width / 60)
        param_font = ImageFont.truetype(resource_path(os.path.join("assert", "Average.ttf")), param_size,
                                        encoding="utf-8")
        # 相机信息
        camera_info = self.context.get_exif_camera_info()

        # 参数信息
        param_content = self.context.get_exif_msg()

        # 计算参数的像素
        param_width, param_height = param_font.getsize(param_content)
        camera_info_width, camera_info_height = camera_font.getsize(camera_info)
        # 计算文字的的坐标
        param_x_axis = frame_width - param_width - self.context.padding_width
        param_y_axis = final_height - self.context.padding_width

        # 计算相机信息的坐标
        camera_info_x_axis = param_x_axis - camera_info_width - camera_info_width / 20
        camera_info_y_axis = param_y_axis

        # 绘制文字
        draw = ImageDraw.Draw(img_new)
        draw.text((param_x_axis, param_y_axis), param_content, fill=self.context.param_color, font=param_font,
                  align="left")
        draw.text((camera_info_x_axis, camera_info_y_axis), camera_info, fill=self.context.camera_info_color,
                  font=camera_font,
                  align="right")

        # 保存图片
        path, file = os.path.split(self.context.source_image_file_path)
        img_new.save(os.path.join(self.context.save_dir, file), img_new.info)
        # 关闭图片
        img_new.close()

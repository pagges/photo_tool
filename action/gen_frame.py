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

        # 文字信息
        text_content = self.context.get_exif_msg()
        text_size = int(width / 50)
        text_font = ImageFont.truetype(resource_path(os.path.join("assert", "Average.ttf")), text_size,
                                       encoding="utf-8")

        # 计算文字的像素
        text_width, text_height = text_font.getsize(text_content)
        # 计算文字的的坐标
        text_x_axis = frame_width - text_width - self.context.padding_width
        text_y_axis = final_height - self.context.padding_width - int(text_height / 4)

        # 绘制文字
        draw = ImageDraw.Draw(img_new)
        draw.text((text_x_axis, text_y_axis), text_content, fill=self.context.text_color, font=text_font,
                  align="center")
        # 保存图片
        path, file = os.path.split(self.context.source_image_file_path)
        img_new.save(os.path.join(self.context.save_dir, file))
        # 关闭图片
        img_new.close()

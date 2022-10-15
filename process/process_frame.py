from loguru import logger

from action.gen_frame import GenFrameAction
from model.context import Context
from util.file_util import *


def process_frame(input_dir, out_dir):
    try:
        if not os.path.exists(out_dir):
            os.mkdir(out_dir)
        # 处理图片
        for image in get_images(input_dir):
            logger.info("process {}", image)
            context = Context(image, out_dir)
            action = GenFrameAction(context)
            action.do_action()
        print("success!\n result file path: " + out_dir)
    except Exception as e:
        logger.error("process error,{}", e)

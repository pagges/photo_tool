from loguru import logger

from action.gen_frame import GenFrameAction
from model.context import Context
from util.file_util import *
from concurrent.futures import ThreadPoolExecutor, as_completed


def process_frame(input_dir, out_dir):
    context_list = []
    try:
        if not os.path.exists(out_dir):
            os.mkdir(out_dir)
        # 处理图片
        for image in get_images(input_dir):
            logger.info("process {}", image)
            context = Context(image, out_dir)
            context_list.append(context)

        with ThreadPoolExecutor(max_workers=8) as t:
            job_list = []
            for context in context_list:
                job = t.submit(action, context)
                job_list.append(job)
        index = 0
        for future in as_completed(job_list):
            future.result()
            index += 1
            if (index == len(job_list)):
                print("success!\n result file path: " + out_dir)
    except Exception as e:
        logger.error("process error,{}", e)


def action(context):
    action = GenFrameAction(context)
    action.do_action()

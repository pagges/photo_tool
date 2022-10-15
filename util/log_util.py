import time
from pathlib import Path
from loguru import logger


def logging():
    project_path = Path.cwd().parent
    log_path = Path(project_path, "log")
    t = time.strftime("%Y_%m_%d")
    logger.add(f"{log_path}/interface_log_{t}.log", rotation="5MB", encoding="utf-8", enqueue=True,
               retention="10 days")
    logger.info("config log")
    return logger
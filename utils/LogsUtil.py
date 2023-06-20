# # @Time : 2021/5/19 15:18
# # @Author: HDM
# # @File : LogsUtil.py
import time
import os
import logging
from loguru import logger


class PropagateHandler(logging.Handler):
    def emit(self, record):
        logging.getLogger(record.name).handle(record)


def get_logger():
    logs_dir = "E:\\pytest\\log"
    timestamp = time.strftime("%Y-%m-%d", time.localtime())
    logFilename = '%s.txt' % timestamp
    log_path = os.path.join(logs_dir, logFilename)
    logger.remove()
    logger.add(log_path)
    logger.add(PropagateHandler())
    return logger


if __name__ == '__main__':
    logger = get_logger()
    logger.info('runlog')

# @Time : 2021/5/19 15:18
# @Author: HDM
# @File : LogsUtil.py
import logging
import logging.handlers
import os
import time


class LogsUtil:
    def __init__(self):
        self.logger = logging.getLogger("")
        # 每次被调用后,清空已经存在handler
        self.logger.handlers.clear()
        # 设置输出的等级
        LEVELS = {'NOTSET': logging.NOTSET,
                  'DEBUG': logging.DEBUG,
                  'INFO': logging.INFO,
                  'WARNING': logging.WARNING,
                  'ERROR': logging.ERROR,
                  'CRITICAL': logging.CRITICAL}
        # 创建文件目录
        logs_dir = "E:\\pytest\\log"
        if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
            pass
        else:
            os.mkdir(logs_dir)
        # 修改log保存位置
        timestamp = time.strftime("%Y-%m-%d", time.localtime())
        logFilename = '%s.txt' % timestamp
        logFilepath = os.path.join(logs_dir, logFilename)
        rotatingFileHandler = logging.handlers.RotatingFileHandler(filename=logFilepath, maxBytes=1024 * 1024 * 50,
                                                                   backupCount=5, encoding="UTF-8")
        # 设置输出格式
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        rotatingFileHandler.setFormatter(formatter)
        # 控制台句柄
        console = logging.StreamHandler()
        console.setLevel(logging.NOTSET)
        console.setFormatter(formatter)
        # 添加内容到日志句柄中
        self.logger.addHandler(rotatingFileHandler)
        self.logger.addHandler(console)
        self.logger.setLevel(logging.NOTSET)
    pass

    def info(self, message):
        self.logger.info(message)
    pass

    def debug(self, message):
        self.logger.debug(message)
    pass

    def warning(self, message):
        self.logger.warning(message)
    pass

    def error(self, message):
        self.logger.error(message)
    pass
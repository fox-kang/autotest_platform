import logging
import os
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


def get_log(log_name):
    # 使用时间戳创建一个新的目录
    dir_name = (os.path.join(os.path.dirname(__file__), f"../log/{timestamp}"))
    os.makedirs(dir_name, exist_ok=True)
    # 设置日志文件夹路径
    log_folder_path = os.path.abspath(dir_name)

    # 创建文件处理器，将此测试用例的日志存入一个单独的文件中
    log_file_path = (os.path.join(os.path.dirname(__file__), f'../log/{timestamp}/{log_name}.log'))
    log_path = os.path.join(log_folder_path, log_file_path)

    # 创建 logger
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.INFO)
    # 创建一个格式器，以设置日志的输出格式
    handler = TimedRotatingFileHandler(log_path, when="D", interval=1, backupCount=3)
    handler.setLevel(logging.INFO)

    # 创建一个 handler，用于写入日志文件
    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(logging.INFO)
    # 创建一个 handler，用于输出到控制台
    stdout_handler = logging.StreamHandler()
    stdout_handler.setLevel(logging.WARNING)

    # 定义 handler 的输出格式
    formatter = logging.Formatter("%(asctime)s\n - %(name)s\n - %(levelname)s\n - %(filename)s\n - %(message)s\n")
    file_handler.setFormatter(formatter)
    stdout_handler.setFormatter(formatter)
    # 给 logger 添加 handler
    logger.addHandler(file_handler)
    logger.addHandler(stdout_handler)

    return logger

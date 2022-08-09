#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/7/7 14:24
# @Author  : 张天宝
# @Email   : boss@xbtit.cn
# @File    : mylog.py
# @Project : 上号器
# @FilePath: E:/pycharmWorkSpace/mytools/上号器\mylog.py

# 自定义日志类
import logging


class MyLog:
    def __init__(self):
        self.logger = logging.getLogger('MyLog')
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)
            # 创建一个handler，用于写入日志文件
            fh = logging.FileHandler('mylog.log', encoding='utf-8')
            fh.setLevel(logging.DEBUG)

            # 再创建一个handler，用于输出到控制台
            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)

            # 定义handler的输出格式
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            # 给logger添加handler
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

    # 记录一条日志
    def debug(self, msg):
        self.logger.debug(msg)

    # 记录一条日志
    def info(self, msg, level=logging.INFO):
        self.logger.log(level, msg)

    # 记录一条日志
    def warning(self, msg, level=logging.WARNING):
        self.logger.log(level, msg)

    # 记录一条日志
    def error(self, msg, level=logging.ERROR):
        self.logger.log(level, msg)

    # 记录一条日志
    def critical(self, msg, level=logging.CRITICAL):
        self.logger.log(level, msg)

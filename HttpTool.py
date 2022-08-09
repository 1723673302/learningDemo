#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/7/7 14:02
# @Author  : 张天宝
# @Email   : boss@xbtit.cn
# @File    : HttpTool.py
# @Project : 上号器
# @FilePath: E:/pycharmWorkSpace/mytools/上号器\HttpTool.py

import json
import urllib.error
import urllib.parse
import urllib.request

import mylog

log = mylog.MyLog()


def get_http(url):
    try:
        # 记录一条日志
        log.debug(f'get_http: {url}')

        response = urllib.request.urlopen(url)
        html = response.read()
        remote_data = json.loads(html)
        if remote_data is None:
            log.debug(f'get_http: {url} is None')
            return None
        if remote_data['code'] is not 200:
            log.debug(f'get_http: {url} code is not 200')
            return None
        log.debug(f'get_http: {url} success')
        return remote_data
    except Exception as e:
        log.error(e)
        return None

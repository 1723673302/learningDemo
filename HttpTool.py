#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/9 10:52
# @Author  : 张天宝
# @Email   : boss@xbtit.cn
# @File    : temp.py
# @Project : learningDemo
# @FilePath: E:/pycharmWorkSpace/github/learningDemo\temp.py


import urllib.error
import urllib.parse
import urllib.request

import mylog

log = mylog.MyLog()


def make_request(url, data):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
        }
        log.debug(f'make_request: {url}')
        log.debug(f'make_request: {data}')
        request = urllib.request.Request(url, headers=headers, data=data)
    except Exception as e:
        log.error(e)
        return None
    return request


# 发送post请求
def post_http(request):
    try:
        response = urllib.request.urlopen(request)
        # html_content = response.readlines()
        # 使用read()读取整个页面内容，使用decode('utf-8')对获取的内容进行编码
        # print(response.read().decode('utf-8'))
        # print(response.status)  # 状态码，判断是否成功,200
        # print(response.getheaders())  # 响应头 得到的一个元组组成的列表
        # print(response.getheader('Server'))  # 得到特定的响应头
        if response.status == 200:
            log.debug(f'post_http: {request.get_full_url()} success')
            return response
        # elif response.status == 404:

        else:
            log.warning(f'post_http: {request.get_full_url()} {response.status}')
            return None
    except Exception as e:
        log.error(f'post_http: {request.get_full_url()} error')
        log.error(f'{e}')
        pass
    # 判断请求是否成功


if __name__ == '__main__':
    # post_http(make_request('http://www.baidu.com', b'123'))
    # post_http(make_request('https://www.xbgit.cn/daohang/', None))
    # post_http(make_request('https://httpbin.org/status/200', None))
    post_http(make_request('https://httpbin.org/status/302', None))
    # post_http(make_request('https://httpbin.org/status/404', None))
    # post_http(make_request('https://httpbin.org/status/502', None))

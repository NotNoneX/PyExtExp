# -*- coding: UTF-8 -*-
# @Time: 2023/9/3 15:46
# @Author: NotNoneX
# @E-mail: NotNoneX@Gmail.com
# @File: decorators.py
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"冰糖提醒: 执行总耗时: {execution_time:.6f} 秒")
        return result

    return wrapper

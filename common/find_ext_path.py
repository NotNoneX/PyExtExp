# -*- coding: UTF-8 -*-
# @Time: 2023/9/2 17:07
# @Author: NotNoneX
# @E-mail: NotNoneX@Gmail.com
# @File: find_ext_path.py

import logging
import os
import types


def find_ext_path(extensions_path) -> types.GeneratorType:
    """
    在指定目录中查找浏览器扩展目录并生成相关信息

    :param extensions_path: 浏览器扩展根路径
    :return: generator: 生成器
    """
    if os.path.exists(extensions_path):
        # 所有扩展
        file_list = os.listdir(extensions_path)
    else:
        return logging.error('---- 请输入正确的浏览器扩展目录 ----')
    crx_num = 0

    # 筛选出目录下的所有扩展目录
    for files in file_list:
        # 所有文件以及目录路径
        files_dir = os.path.join(extensions_path, files)
        is_directory = os.path.isdir(files_dir)
        if is_directory:
            crx_num += 1
            yield files_dir
    logging.info(msg=f'共找到{crx_num}个扩展')

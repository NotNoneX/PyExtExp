# -*- coding: UTF-8 -*-
# @Time: 2023/9/2 16:28
# @Author: NotNoneX
# @E-mail: NotNoneX@Gmail.com
# @File: create_crx.py
import logging
import os

from crx3 import creator

from common.find_ext_path import find_ext_path
from common.get_config import get_config
from common.get_ext_info import get_ext_info

logging.basicConfig(level=logging.INFO)


def create_crx():
    """

    :return: crx
    """
    num = 0
    config_dict = get_config()
    if config_dict['browser_type'].lower() == 'chrome':
        extensions_dir = config_dict['extensions_dir']
        # 获取扩展目录
        ext_path = find_ext_path(extensions_dir)
        # 取得插件信息
        ext_info = get_ext_info(ext_path)
        # 从配置中获取私钥和扩展保存目录
        for crx_dir, crx_name, crx_version in ext_info:
            pem_name = crx_name + '_' + crx_version + '_' + '.pem'
            crx_name = crx_name + '_' + crx_version + '_' + '.crx'
            pem_path = os.path.join(config_dict['pem_path'], pem_name)
            crx_path = os.path.join(config_dict['crx_path'], crx_name)
            # print(os.path.sep)
            # 私钥与扩展目录是否存在
            if not os.path.exists(os.path.split(pem_path)[0]):
                os.makedirs(os.path.split(pem_path)[0])
            if not os.path.exists(os.path.split(crx_path)[0]):
                os.makedirs(os.path.split(crx_path)[0])
            try:
                # 生成私钥文件
                creator.create_private_key_file(pem_path)
            except Exception as e:
                logging.error("发生了意想不到的错误: " + str(e))
            else:
                try:
                    num += 1
                    print(f'正在处理第{num}个插件')
                    # 生成浏览器扩展文件
                    creator.create_crx_file(crx_dir, private_key_file=pem_path, output_file=crx_path)
                except Exception as e:
                    logging.error("发生了意想不到的错误: " + str(e))

    logging.info('---- 程序运行结束! ----')

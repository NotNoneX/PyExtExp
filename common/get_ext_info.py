# -*- coding: UTF-8 -*-
# @Time: 2023/9/3 4:26
# @Author: NotNoneX
# @E-mail: NotNoneX@Gmail.com
# @File: get_ext_info.py
import json
import logging
import os
import re
import types


def get_ext_info(ext_list: list or types.GeneratorType) -> types.GeneratorType:
    """

    :param ext_list: 扩展列表
    :return: 扩展信息
    """

    if not (isinstance(ext_list, list) or isinstance(ext_list, types.GeneratorType)):
        raise TypeError('参数有误，参数类型只能为list或generator')
    # 取得每个扩展目录
    for crx_dir in ext_list:
        # 读取目录下的文件列表
        files_list = os.listdir(crx_dir)
        # 判断是否为版本号目录
        for vers in files_list:
            version = ''
            crx_name = ''
            rel_path = os.path.join(crx_dir, vers)
            # 排除文件 保留版本号目录
            if os.path.isdir(rel_path):
                # 读取manifest.json文件获取扩展名
                try:
                    manifest_path = os.path.join(rel_path, 'manifest.json')
                    with open(manifest_path, 'r', encoding='utf8') as json_data:
                        try:
                            info = json.load(json_data)
                        except json.JSONDecodeError as fal:
                            logging.error(f'JSON解码错误: {fal}')
                except FileNotFoundError as e:
                    logging.error(f'文件未找到错误: {e}')
                    crx_name = os.path.split(rel_path)[0].split(os.path.sep)[-1]
                else:

                    name = info['name']
                    if '__MSG' in name:
                        regex = f'(?<=__MSG_).*(?=__)'
                        # logging.info(rel_path)
                        # logging.info(name)
                        # 中文配置文件路径
                        zh_cfg_path = os.path.join(rel_path, '_locales', 'zh_CN', 'messages.json')
                        en_cfg_path = os.path.join(rel_path, '_locales', 'en', 'messages.json')
                        if os.path.exists(zh_cfg_path):
                            config_path = zh_cfg_path
                        else:
                            config_path = en_cfg_path
                        code_name = re.search(regex, name).group()
                        try:
                            with open(config_path, 'r', encoding='utf8') as cfg_file:
                                try:
                                    zh = json.load(cfg_file)
                                except json.JSONDecodeError as fal:
                                    logging.error(str(fal))
                        except FileNotFoundError as e:
                            logging.error(f'加载配置时出错: {e}')
                        else:
                            name = zh[code_name]['message']
                            crx_name = name
                    else:
                        crx_name = info['name']
                    version = info['version']

                yield rel_path, crx_name, version

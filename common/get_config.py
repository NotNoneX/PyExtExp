# -*- coding: UTF-8 -*-
# @Time: 2023/9/3 4:28
# @Author: NotNoneX
# @E-mail: NotNoneX@Gmail.com
# @File: get_config.py
import configparser
import os


def get_config() -> dict:
    """

    :return: dict: config
    """
    root_dir = os.path.split(os.path.split(__file__)[0])[0]
    conf_path = os.path.join(root_dir, 'config.ini')
    if not os.path.exists(conf_path):
        raise FileNotFoundError
    config = configparser.ConfigParser()
    config.read(conf_path, encoding='utf8')

    browser_type = config['Browser']['Type']
    conf_dict = dict(config['Options'].items())
    conf_dict['browser_type'] = browser_type
    return conf_dict

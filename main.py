# -*- coding: UTF-8 -*-
# @Time: 2023/9/3 4:36
# @Author: NotNoneX
# @E-mail: NotNoneX@Gmail.com
# @File: main.py
from common.create_crx import create_crx
from common.decorators import timer


# 开始执行

@timer
def generate_crx():
    create_crx()


if __name__ == '__main__':
    generate_crx()

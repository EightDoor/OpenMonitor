#!/usr/bin/python3
# -*- coding:utf-8 -*-
from PIL import Image

async def generate_ico(ico_path: str, sizes = [(64,64), (128,128), (256, 256)]):
    """
        将图片转换为ICO
        :params ico_path: 图片路径
        :params sizes ICO尺寸
    """
    # 打开图片
    with Image.open(ico_path, 'r') as f:
        ico_path = ''
        f.save(ico_path, format='ICO', sizes = sizes)
        return ico_path
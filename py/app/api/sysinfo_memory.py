#!/usr/bin/python3
# -*- coding: utf-8 -*-
import psutil


# 内存信息
def get_memory_info():
    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()
    return {
        "usage": memory.percent,
        "swap_usage": swap.percent,
    }
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import psutil


# 内存信息
def get_memory_info():
    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()
    return {
        "memory": {
            "total": memory.total,
            "available": memory.available,
            "usage": memory.percent,
            "other": {
                "used": memory.used,
                "free": memory.free,
                "active": memory.active,
                "inactive": memory.inactive,
                "buffers": memory.buffers,
                "cached": memory.cached,
                "shared": memory.shared,
                "slab": memory.slab
            }
        },
        "swap": {
            "usage": swap.percent,
            "total": swap.total,
            "used": swap.used,
            "free": swap.free,
            "sin": swap.sin,
            "sout": swap.sout
        },
    }

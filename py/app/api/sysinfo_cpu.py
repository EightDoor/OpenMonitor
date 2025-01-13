#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import subprocess

import psutil


# CPU信息
def get_cpu_info():
    cpu_usage = psutil.cpu_percent()
    cpu_count = psutil.cpu_count()
    # load_avg = os.getloadavg()
    return {
        "usage": cpu_usage,
        "count": cpu_count,
    }

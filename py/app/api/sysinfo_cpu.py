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

def average_load():
    """平均负载 1分钟、5分钟、15分钟"""
    avg1,avg5, avg15 = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
    return {
        "avg1": avg1,
        "avg5": avg5,
        "avg15": avg15
    }
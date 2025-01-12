#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import subprocess

import psutil


# 温度获取
def get_cpu_temperature():
    try:
        # 使用 psutil 获取传感器温度
        temps = psutil.sensors_temperatures()
        if "coretemp" in temps:  # 常见的 CPU 温度来源
            core_temps = temps["coretemp"]
            avg_temp = sum([t.current for t in core_temps]) / len(core_temps)
            return {"average_temperature": avg_temp, "details": core_temps}
        else:
            return {"error": "No coretemp sensor data available"}
    except Exception:
        # 如果 psutil 不可用，尝试调用 sensors 工具
        try:
            result = subprocess.run(["sensors"], capture_output=True, text=True)
            return {"output": result.stdout}
        except FileNotFoundError:
            return {"error": "sensors command not found, install lm-sensors"}


# CPU信息
def get_cpu_info():
    cpu_usage = psutil.cpu_percent()
    cpu_count = psutil.cpu_count()
    # load_avg = os.getloadavg()
    return {
        "usage": cpu_usage,
        "count": cpu_count,
        # "load": load_avg,
        # CPU温度需要硬件支持，可以使用第三方工具如 `sensors`
        # "temperature": get_cpu_temperature(),
    }

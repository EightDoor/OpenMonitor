#!/usr/bin/python3
# -*- coding: utf-8 -*-
import subprocess

import psutil


# 磁盘信息
def get_disk_info(disk="/"):
    disk_usage = psutil.disk_usage(disk)
    disk_io = psutil.disk_io_counters()
    # 磁盘温度和SMART状态可以通过工具如 smartmontools 获取，需调用外部命令
    return {
        "usage": disk_usage.percent,
        "read_bytes": disk_io.read_bytes,
        "write_bytes": disk_io.write_bytes,
        "temperature": get_disk_temperature,
    }


# 获取磁盘温度
def get_disk_temperature(disk="/dev/sda"):
    try:
        # 使用 smartctl 获取硬盘温度信息
        result = subprocess.run(
            ["smartctl", "-A", disk], capture_output=True, text=True, check=True
        )
        # 解析温度信息
        for line in result.stdout.split("\n"):
            if "Temperature_Celsius" in line:
                parts = line.split()
                temperature = parts[-1]  # 温度通常是最后一列
                return {"disk": disk, "temperature": int(temperature)}
        return {"disk": disk, "temperature": "Not available"}
    except FileNotFoundError:
        return {"error": "smartctl not found. Install smartmontools."}
    except subprocess.CalledProcessError as e:
        return {"error": e.stderr}


# 磁盘SMART状态获取
def get_disk_smart_status(disk="/dev/sda"):
    try:
        # 调用 smartctl 工具获取 SMART 状态
        result = subprocess.run(
            ["smartctl", "-H", disk], capture_output=True, text=True, check=True
        )
        # 提取健康状态
        if "PASSED" in result.stdout:
            return {"disk": disk, "smart_status": "PASSED"}
        else:
            return {"disk": disk, "smart_status": "FAILED"}
    except FileNotFoundError:
        return {"error": "smartctl not found, install smartmontools"}
    except subprocess.CalledProcessError as e:
        return {"error": e.stderr}


def get_physical_disks():
    result = psutil.disk_partitions()
    return result

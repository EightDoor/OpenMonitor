#!/usr/bin/python3
# -*- coding: utf-8 -*-
import subprocess

import psutil
import asyncio


# 磁盘信息
def get_disk_info(path="/"):
    disk_usage = psutil.disk_usage(path)
    # 磁盘温度和SMART状态可以通过工具如 smartmontools 获取，需调用外部命令
    return {
        "total": disk_usage.total,
        "used": disk_usage.used,
        "free": disk_usage.free,
        "usage": disk_usage.percent,
        "temperature": get_disk_temperature(path),
    }


# 磁盘io信息
async def get_disk_io():
    prev_counters = psutil.disk_io_counters()
    await asyncio.sleep(1)
    curr_counters = psutil.disk_io_counters()
     # 增量计算
    read_count_diff = curr_counters.read_count - prev_counters.read_count
    write_count_diff = curr_counters.write_count - prev_counters.write_count
    read_time_diff = curr_counters.read_time - prev_counters.read_time
    write_time_diff = curr_counters.write_time - prev_counters.write_time
    read_bytes = curr_counters.read_bytes - prev_counters.read_bytes
    write_bytes = curr_counters.write_bytes - prev_counters.write_bytes
    
    # 避免除零错误
    read_latency = read_time_diff / read_count_diff if read_count_diff > 0 else 0
    write_latency = write_time_diff / write_count_diff if write_count_diff > 0 else 0
    return {
        "read_count": read_count_diff,
        "write_count": write_count_diff,
        "read_latency": read_latency,
        "write_latency": write_latency,
        "read_bytes": read_bytes,
        "write_bytes": write_bytes
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


# 获取磁盘列表
def get_physical_disks():
    result = psutil.disk_partitions()
    return filter_valid_mount_points(result)


# 过滤有效挂载点
def filter_valid_mount_points(mount_points):
    valid_mounts = []
    for mount in mount_points:
        device, path, fs_type, options = mount
        # 判断是否可写，排除“squashfs”文件系统，且挂载路径不应包含“/snap”
        if "rw" in options and fs_type != "squashfs" and not path.startswith("/snap"):
            valid_mounts.append(mount)
    return valid_mounts

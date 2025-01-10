#!/usr/bin/python3
# -*- coding:utf-8 -*-
import subprocess


# 系统日志获取
def get_system_logs(lines=10):
    try:
        # 使用 journalctl 获取最新的系统日志
        result = subprocess.run(
            ["journalctl", "-n", str(lines)], capture_output=True, text=True
        )
        return {"logs": result.stdout.split("\n")}
    except FileNotFoundError:
        return {"error": "journalctl command not found"}

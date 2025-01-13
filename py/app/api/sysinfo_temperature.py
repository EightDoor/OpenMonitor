#!/usr/bin/python3
# -*- coding: utf-8 -*-

import psutil

def get_temp():
    """获取硬件温度"""
    temperatures = psutil.sensors_temperatures()
    sensors_fans = psutil.sensors_fans()
    return {
        "temperatures": temperatures,
        "sensors_fans": sensors_fans
    }
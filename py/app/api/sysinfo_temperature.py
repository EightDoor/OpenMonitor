#!/usr/bin/python3
# -*- coding: utf-8 -*-

import psutil
import logging

logger = logging.getLogger(__name__)

def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return f"{int(hh)}:{int(mm):02}:{int(ss):02}"

def get_temp():
    """获取传感器数据"""
    result = {
        "temperatures": {},
        "fans": {},
        "battery": {}
    }
    temps = psutil.sensors_temperatures()
    fans = psutil.sensors_fans() if hasattr(psutil, "sensors_fans") else {}
    battery = psutil.sensors_battery()
    
    names = set(list(temps.keys()) + list(fans.keys()))
    for name in names:
        logger.debug(name)
        # 温度
        if name in temps:
            for entry in temps[name]:
                result[name]['temperatures']['current'] = f"{entry.current}℃"
                result[name]['temperatures']['high'] = f"{entry.high}℃"
                result[name]['temperatures']['critical'] = f"{entry.critical}℃"

        # 风扇
        if name in fans:    
            for entry in fans[name]:
                result[name]['fans']['current'] = f"{entry.current} RPM"
    
    result['battery']['charge'] = round(battery.percent, 2)
    if battery.power_plugged:
        result['battery']['pluggedIn'] = "yes"
        result['battery']['status'] = "充电中" if battery.percent < 100 else "已充满"
    else:
        result['battery']['status'] = "离线"
        result['battery']['pluggedIn'] = "no"
    return result
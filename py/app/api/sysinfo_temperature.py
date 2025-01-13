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
    result = []
    temps = psutil.sensors_temperatures()
    fans = psutil.sensors_fans() if hasattr(psutil, "sensors_fans") else {}
    battery = psutil.sensors_battery()
    
    names = set(list(temps.keys()) + list(fans.keys()))
    for name in names:
        logger.debug(name)
        # 温度
        if name in temps:
            for entry in temps[name]:
                result.append({
                    "name": name,
                    "temperatures": {
                        "current": f"{entry.current}℃",
                        "high":  f"{entry.high}℃",
                        "critical": f"{entry.critical}℃"
                    }
                })

        # 风扇
        if name in fans:    
            for entry in fans[name]:
                result.append({
                    "name": name,
                    "fans": {
                        "current"f"{entry.current} RPM"
                    }
                })
    
    battery_result = {
        "charge": 0,
        "pluggedIn": "",
        "status": ""
    }
    battery_result['charge'] = round(battery.percent, 2)
    if battery.power_plugged:
        battery_result['pluggedIn'] = "yes"
        battery_result['status'] = "充电中" if battery.percent < 100 else "已充满"
    else:
        battery_result['status'] = "离线"
        battery_result['pluggedIn'] = "no"
    result.append(battery_result)
    return result
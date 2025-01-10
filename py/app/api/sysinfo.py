#!/usr/bin/python3
# -*- coding:utf-8 -*-



from app.api.sysinfo_cpu import get_cpu_info
from app.api.sysinfo_dist import get_disk_info
from app.api.sysinfo_memory import get_memory_info
from app.api.sysinfo_network import get_network_info
from app.api.sysinfo_send_email import check_and_send_alert


async def monitor():
    cpu_info = get_cpu_info()
    memory_info = get_memory_info()
    disk_info = get_disk_info()
    network_info = get_network_info()

    info = {
        "cpu": cpu_info,
        "memory": memory_info,
        "disk": disk_info,
        "network": network_info,
    }

    check_and_send_alert(info)  # 检查是否需要发送预警
    return info

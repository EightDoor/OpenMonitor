#!/usr/bin/python3
# -*- coding:utf-8 -*-
from fastapi import APIRouter
from app import result
from app.api import sysinfo
from app.api.sysinfo_log import get_system_logs
from app.api.sysinfo_dist import get_disk_smart_status
from app.api.sysinfo_network import get_network_quality_with_pingparsing
from app.api.sysinfo_dist import get_physical_disks

router = APIRouter()


@router.get("/")
def hello():
    return result.success("hello world")


@router.get("/sysinfo")
async def get_cpu_info():
    """获取cpu信息"""
    res = await sysinfo.monitor()
    return result.success(res)


@router.get("/sysinfo_log")
def get_sysinfo_log():
    """获取系统日志"""
    res = get_system_logs()
    return result.success(res)


@router.get("/get_disk_smart_status")
def disk_smart_status(disk: str):
    """获取磁盘状态"""
    res = get_disk_smart_status(disk)
    return result.success(res)


@router.get("/get_network_quality_with_pingparsing")
def network_quality_with_pingparsing():
    """丢包率 (packet_loss_rate) 和 平均延迟 (latency)"""
    res = get_network_quality_with_pingparsing()
    return result.success(res)


@router.get("/list_disks")
def list_disks():
    """磁盘列表"""
    res = get_physical_disks()
    return result.success(res)

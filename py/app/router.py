#!/usr/bin/python3
# -*- coding:utf-8 -*-
from fastapi import APIRouter
from app import result
from app.api import (
    sysinfo_cpu,
    sysinfo_network,
    sysinfo_dist,
    sysinfo_log,
    sysinfo_memory,
    sysinfo_send_email,
)

router = APIRouter()


@router.get("/")
def hello():
    return result.success("hello world")


@router.get("/get_cpu_info")
def get_cpu_info():
    """获取cpu信息"""
    res = sysinfo_cpu.get_cpu_info()
    return result.success(res)


@router.get("/get_disk_info")
def get_disk_info(path: str):
    """获取磁盘信息"""
    res = sysinfo_dist.get_disk_info(path)
    return result.success(res)

@router.get("/get_disk_io")
def get_disk_io():
    """获取磁盘 IO"""
    res = sysinfo_dist.get_disk_io()
    return result.success(res)

@router.get("/get_memory_info")
def get_memory_info():
    """获取内存信息"""
    res = sysinfo_memory.get_memory_info()
    return result.success(res)


@router.get("/get_network_info")
def get_network_info():
    """获取网络信息"""
    res = sysinfo_network.get_network_info()
    return result.success(res)


@router.get("/sysinfo_log")
def get_sysinfo_log():
    """获取系统日志"""
    res = sysinfo_log.get_system_logs()
    return result.success(res)


@router.get("/get_disk_smart_status")
def disk_smart_status(disk: str):
    """获取磁盘状态"""
    res = sysinfo_dist.get_disk_smart_status(disk)
    return result.success(res)


@router.get("/get_network_quality_with_pingparsing")
def network_quality_with_pingparsing():
    """丢包率 (packet_loss_rate) 和 平均延迟 (latency)"""
    res = sysinfo_network.get_network_quality_with_pingparsing()
    return result.success(res)


@router.get("/list_disks")
def list_disks():
    """磁盘列表"""
    res = sysinfo_dist.get_physical_disks()
    return result.success(res)

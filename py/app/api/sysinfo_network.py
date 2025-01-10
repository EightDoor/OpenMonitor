#!/usr/bin/python3
# -*- coding: utf-8 -*-


import pingparsing
import psutil


# ping 命令来测量网络的 丢包率 (packet_loss_rate) 和 平均延迟 (latency)
def get_network_quality_with_pingparsing(host="8.8.8.8", count=4):
    ping_parser = pingparsing.PingParsing()
    transmitter = pingparsing.PingTransmitter()
    transmitter.destination = host
    transmitter.count = count

    try:
        result = transmitter.ping()
        stats = ping_parser.parse(result).as_dict()
        return {
            "host": host,
            "packet_loss_rate": stats.get("packet_loss_rate", "Unavailable"),
            "latency": stats.get("rtt_avg", "Unavailable"),
        }
    except Exception as e:
        return {"error": str(e)}


# 网络信息
def get_network_info():
    net_io = psutil.net_io_counters()
    # 丢包率、延迟、连接数需结合 `ping` 或系统工具实现
    return {
        "throughput": {
            "bytes_sent": net_io.bytes_sent,
            "bytes_recv": net_io.bytes_recv,
        },
        "connections": len(psutil.net_connections()),
    }

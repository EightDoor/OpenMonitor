#!/usr/bin/python3
# -*- coding:utf-8 -*-
import smtplib
from email.header import Header
from email.mime.text import MIMEText

# 邮件配置
EMAIL_HOST = "smtp.your-email-provider.com"
EMAIL_PORT = 587
EMAIL_USER = "your_email@example.com"
EMAIL_PASSWORD = "your_password"
EMAIL_RECEIVER = "receiver_email@example.com"


# 检查并发送邮件
def check_and_send_alert(info):
    # 设定阈值
    thresholds = {
        "cpu_usage": 90,
        "memory_usage": 90,
        "disk_usage": 90,
    }
    alerts = []

    # 检查CPU
    if info["cpu"]["usage"] > thresholds["cpu_usage"]:
        alerts.append(f"CPU usage is high: {info['cpu']['usage']}%")
    # 检查内存
    if info["memory"]["usage"] > thresholds["memory_usage"]:
        alerts.append(f"Memory usage is high: {info['memory']['usage']}%")
    # 检查磁盘
    if info["disk"]["usage"] > thresholds["disk_usage"]:
        alerts.append(f"Disk usage is high: {info['disk']['usage']}%")

    # 如果有告警，发送邮件
    if alerts:
        send_email("\n".join(alerts))


# 发送邮件方法
def send_email(message):
    msg = MIMEText(message, "plain", "utf-8")
    msg["From"] = Header(EMAIL_USER, "utf-8")
    msg["To"] = Header(EMAIL_RECEIVER, "utf-8")
    msg["Subject"] = Header("Server Alert", "utf-8")

    with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USER, EMAIL_RECEIVER, msg.as_string())

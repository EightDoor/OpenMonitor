# 简介
- 服务器监控 python
- 使用库
  - [psutil（进程和系统实用程序）](https://github.com/giampaolo/psutil)
# 下载依赖
- [使用uv管理](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer)
- 安装 `pip install uv`
- 启动 `uv run main.py`

# 系统依赖
- cpu温度获取：`lm-sensors`
- 磁盘检查：`smartmontools`
- 获取磁盘列表 `diskutil`
  - smartctl -H /dev/sda
  ```text
  # smart_status状态
  状态	含义	描述
  PASSED	健康良好	磁盘正常工作，未发现任何故障迹象。
  FAILED	健康状况不良	磁盘检测到严重问题，可能即将失败。
  PRE-FAIL	潜在故障，预警	检测到可能导致故障的潜在问题，建议备份。
  UNKNOWN	无法获取健康状态	无法获取SMART数据，可能是硬件或接口问题。
  N/A	不适用或无法获取状态	磁盘不支持 SMART 或状态无法访问。
  ```
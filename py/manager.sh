#!/bin/bash

# 检查是否以 root 用户运行
if [ "$(id -u)" -ne 0 ]; then
  echo "请以 root 用户运行此脚本。"
  exit 1
fi

# 获取当前脚本所在目录的绝对路径
SCRIPT_DIR=$(pwd)
SCRIPT_NAME="main.py"
SERVICE_NAME="monitor-py"

# 设置 Python 脚本的路径
SCRIPT_PATH="$SCRIPT_DIR/$SCRIPT_NAME"

# 检查 Python 脚本是否存在
if [ ! -f "$SCRIPT_PATH" ]; then
  echo "Python 脚本 $SCRIPT_NAME 不存在，请确保脚本在当前目录。"
  exit 1
fi

# 提示选择操作
echo "请选择操作:"
echo "1) 安装并启动服务"
echo "2) 停止服务"
echo "3) 禁用开机自启"
echo "4) 删除服务文件"
echo "5) 重启服务"
echo "6) 查看服务状态"
echo "7) 查看服务日志"
echo "8) 退出"
read -p "请输入选项 (1-8): " ACTION

case $ACTION in
  1) 
    # 创建 Systemd 服务文件
    SERVICE_FILE="/etc/systemd/system/$SERVICE_NAME.service"
    echo "创建 Systemd 服务文件 $SERVICE_FILE..."
  
    cat <<EOF > $SERVICE_FILE
[Unit]
Description=Your Python Program
After=network.target

[Service]
#ExecStart=/usr/bin/python3 $SCRIPT_PATH
ExecStart=/root/miniconda3/bin/python $SCRIPT_PATH
WorkingDirectory=$SCRIPT_DIR
Restart=always
User=$(whoami)
Group=$(whoami)

[Install]
WantedBy=multi-user.target
EOF
  
    # 重新加载 Systemd 配置
    echo "重新加载 Systemd 配置..."
    systemctl daemon-reload

    # 启动服务并设置开机自启
    echo "启动服务并设置开机自启..."
    systemctl start $SERVICE_NAME
    systemctl enable $SERVICE_NAME

    # 打印状态
    systemctl status $SERVICE_NAME

    echo "服务已成功启动并设置为开机自启。"
    ;;

  2) 
    # 停止服务
    echo "停止服务 $SERVICE_NAME..."
    systemctl stop $SERVICE_NAME
    echo "服务已停止。"
    ;;

  3) 
    # 禁用开机自启
    echo "禁用服务 $SERVICE_NAME 的开机自启..."
    systemctl disable $SERVICE_NAME
    echo "服务已禁用开机自启。"
    ;;

  4) 
    # 删除服务文件
    echo "删除服务文件 $SERVICE_NAME..."
    systemctl stop $SERVICE_NAME
    systemctl disable $SERVICE_NAME
    rm -f /etc/systemd/system/$SERVICE_NAME.service
    systemctl daemon-reload
    echo "服务文件已删除，服务已停止并禁用。"
    ;;

  5) 
    # 重启服务
    echo "重启服务 $SERVICE_NAME..."
    systemctl restart $SERVICE_NAME
    echo "服务已重启。"
    ;;

  6)
    # 查看服务状态
    echo "查看服务 $SERVICE_NAME 状态..."
    systemctl status $SERVICE_NAME
    ;;

  7)
    # 查看服务日志
    echo "查看服务 $SERVICE_NAME 的日志..."
    journalctl -u $SERVICE_NAME -n 100 --no-pager
    ;;

  8)
    # 退出脚本
    echo "退出脚本。"
    exit 0
    ;;

  *)
    echo "无效选项，请输入 1 到 8 之间的数字。"
    exit 1
    ;;
esac
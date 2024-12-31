# 简介
- 服务器监控 python
- 使用库
  - [psutil（进程和系统实用程序）](https://github.com/giampaolo/psutil)
# 生成requirements.txt
- pipreqs 根据项目文件中的实际导入来生成依赖列表
- pip安装依赖 `pip install pipreqs`
- 执行 `pipreqs ./ --encoding=utf-8`
#!/usr/bin/python3
# -*- coding:utf-8 -*-
import psutil
from pydantic import BaseModel
from typing import Any

class AllInfo(BaseModel):
    cpuTimes: Any

async def all_info():
    pass

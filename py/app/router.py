#!/usr/bin/python3
# -*- coding:utf-8 -*-
from fastapi import FastAPI, APIRouter
from app import result
from api import cpu_info


router = APIRouter()

@router.get("/")
def hello():
    return result.success('hello world')

@router.get("/cpu")
async def get_cpu_info():
    """获取cpu信息"""
    res = await cpu_info.all_info()
    return result.success(res)
    pass
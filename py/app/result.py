#!/usr/bin/python3
# -*- coding:utf-8 -*-

def success(data: any, *, msg = 'success', code = 0):
    """
        成功
    """
    return {
        "data": data,
        "msg": msg,
        "code": code
    }
    
def error(data: any, *,  msg = 'success', code = 0):
    """
        失败
    """
    return {
        "data": data,
        "msg": msg,
        "code": code
    }
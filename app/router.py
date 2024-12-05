#!/usr/bin/python3
# -*- coding:utf-8 -*-
from fastapi import FastAPI, APIRouter
from app import result
from app.api import ip_address
from typing import Union


router = APIRouter()

@router.get("/")
def hello():
    return result.success('hello world')

@router.get('/address_inquiry')
async def address_inquiry(ip: Union[str, None] = None, type: Union[int, None] = None):
    res = await ip_address.address_information(ip, type=type)
    return result.success(res)

@router.get('/generate_ico')
async def generate_ico():
    
    pass
#!/usr/bin/python3
# -*- coding:utf-8 -*-
from fastapi import FastAPI, APIRouter
from app import result


router = APIRouter()

@router.get("/")
def hello():
    return result.success('hello world')
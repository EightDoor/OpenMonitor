#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient


def get_database():
    user = "zhoukai"
    passwd = "123456"
    host = "192.168.192.3"
    port = "27017"
    CONNECTION_STRING = f"mongodb://{user}:{passwd}@{host}:{port}"
    client = MongoClient(CONNECTION_STRING)
    return client


if __name__ == "__main__":
    dbname = get_database()
    print(dbname)
    pass

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/4/6 下午6:54
# @Author  : ZHZ
import time

def timeStampToDate(timeStamp):
    timeArray = time.localtime(int(timeStamp))
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime


#print timeStampToDate(1460038474)
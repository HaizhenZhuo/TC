#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/4/6 下午6:54
# @Author  : ZHZ
import time
import pandas as pd

def timeStampToDate(timeStamp):
    timeArray = time.localtime(int(timeStamp))
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime

#生成start-end之间的日期作为列
def datetimeColumnsGenerate(start,end):
    date = pd.date_range(start,end)
    columns = [x.strftime('%Y-%m-%d') for x in date]
    return columns

#生成二维dict
def addtwodimdict(thedict, key_a, key_b, val):
    if key_a in thedict:
        thedict[key_a].update({key_b: val})
    else:
        thedict.update({key_a:{key_b: val}})

#print timeStampToDate(1460038474)
# print datetimeColumnsGenerate('2015-03-01','2015-03-03')
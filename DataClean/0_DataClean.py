#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/4/6 下午6:58
# @Author  : ZHZ

import pandas as pd
import numpy as np
from Util import DataCleanUtil

#读取数据,columns默认为空
songs = pd.read_csv("../Data/mars_tianchi_songs.csv",header=None)
actions = pd.read_csv("../Data/mars_tianchi_user_actions.csv",header=None)

#重命名列名
def renameColumns():
    songs.columns = ['song_id','artist_id','publish_time','song_init_plays','Language','Gender']
    actions.columns = ['user_id','song_id','gmt_create_timestamp','action_type','Ds']

#将actions里的每一条时间戳数据转换成YYMMDD_HHMMSS形式,保留原有的timestamp是为了方便时间截取
def transformTimeStampToDate():
    actions['gmt_create_date']=actions['gmt_create_timestamp'].map(lambda x : DataCleanUtil.timeStampToDate(x))

#将处理过的数据保存在OutputFile中
def saveToFile():
    songs.to_csv('../Data/OutputFile/0_songs.csv',index=False)
    actions.to_csv('../Data/OutputFile/0_actions.csv',index=False)


if __name__ == '__main__':
    renameColumns()
    transformTimeStampToDate()
    saveToFile()
    print actions.columns
    print actions['gmt_create_date'].head(5)



'''
users_value_counts = actions.user_id.value_counts()
action1 = actions[actions['action_type']==1]
action2 = actions[actions['action_type']==2]
action3 = actions[actions['action_type']==3]
'''




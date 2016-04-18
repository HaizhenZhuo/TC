#-*- coding:utf8 -*-

import pandas as pd
import numpy as np
from datetime import datetime
from Util import DataCleanUtil

#读文件
file = pd.read_csv('../Data/OutputFile/0_1_actions.csv')
date = DataCleanUtil.datetimeColumnsGenerate('2015-03-01','2015-08-30')
result = {}

file = file[['song_id','action_type','gmt_create_date']]
file['gmt_create_date'] = file['gmt_create_date'].map(lambda x:x.split(' ')[0])

#过滤每种action type
def transferActionType(action,type):
    action = int(action)
    if action==type:
        return type
    else:
        return 0

#统计对应类型的计数playcount,downloadcount,collectcount
def createTypeCount(file,type):
    file['action_type']=file['action_type'].map(lambda x:transferActionType(x,type))
    file = file.groupby(['song_id','gmt_create_date']).sum()/type
    file =file.unstack()
    file.columns = date
    return file

def save(file,type):
    typeset = ['play','download','collect']
    path = '../Data/OutputFile/1_'+typeset[type-1]+'count.csv'
    file.to_csv(path,na_rep='0.0')

#统计3种action的操作数目
def actionStats():
    tmp = file.groupby(['song_id','gmt_create_date'])
    for (k1,k2),group in tmp:
        play = group[group['action_type']==1]['action_type'].count()
        download = group[group['action_type']==2]['action_type'].count()
        collect = group[group['action_type']==3]['action_type'].count()
        val = str(play)+';'+str(download)+';'+str(collect)
        DataCleanUtil.addtwodimdict(result,k2,k1,val)
    count = pd.DataFrame(result)
    count.to_csv('../Data/OutputFile/1_action_stats.csv',na_rep='0;0;0')

if __name__=='__main__':
    #这三种每次只能执行一种，连续执行会报错……
    # file = createTypeCount(file,1)
    # save(file,1)
    # file = createTypeCount(file,2)
    # save(file,2)
    # file = createTypeCount(file,3)
    # save(file,3)
    actionStats()
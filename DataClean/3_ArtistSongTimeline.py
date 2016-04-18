# -*- coding: utf-8 -*-
import pandas as pd
from datetime import datetime
from Util import DataCleanUtil

#读取数据
file = pd.read_csv('../Data/OutputFile/0_1_songs.csv')

#选取对应的列
frame = file[['artist_id','song_id','publish_time']]

#生成2015-03-01～2015-09-30计算从歌曲发型到对应日期的天数
date = DataCleanUtil.datetimeColumnsGenerate('3/1/2015','10/30/2015')
columns = ['artist_id','song_id','publish_time','tmp','isold']+date
frame = frame.reindex(columns=columns)

#将publish_time列设置成datetime格式
frame['publish_time'] = frame['publish_time'].map(lambda x:str(x)[:4]+'-'+str(x)[4:6]+'-'+str(x)[6:])
frame['publish_time'] = frame['publish_time'].map(lambda x:datetime.strptime(x,'%Y-%m-%d'))

#计算（2015-03-01）-publish_time = 发行了多少时间
frame['tmp'] = '2015-03-01'
frame['tmp'] = frame['tmp'].map(lambda x:datetime.strptime(x,'%Y-%m-%d'))
frame['tmp'] = frame['tmp']-frame['publish_time']
frame['tmp'] = frame['tmp'].map(lambda x:x.days)

#属性构造：当前时间-publish_time = 发行了多少时间
for i,x in enumerate(date):
    frame[x] = frame['tmp']+i

#添加对应歌曲是否是老歌（True-是，规则-至2015-03-01发现时间>90)
frame['isold'] = frame['tmp']>90

frame = frame.drop('tmp',axis=1)
frame.to_csv('../Data/OutputFile/3_timeline.csv',index=False)

#-*- coding: utf8 -*-
import pandas as pd
from Util import DataCleanUtil

song_play_count = pd.read_csv('../Data/OutputFile/1_playcount.csv')
song = pd.read_csv('../Data/OutputFile/0_1_songs.csv')
date = DataCleanUtil.datetimeColumnsGenerate('2015-03-01','2015-08-30')
result = {}

#根据song_id合并两张表，基于对song_id的统计，做artist的统计
artist_play = pd.merge(song_play_count,song,how='left',on='song_id')
#截取列（只取song表的artist_id列）
artist_play = artist_play.ix[:,:185]

tmp = artist_play.groupby('artist_id')
for i,group in tmp:
    for d in date:
        val = tmp[d].sum()
        DataCleanUtil.addtwodimdict(result,d,i,val[i])

sum = pd.DataFrame(result)
sum.to_csv('../Data/OutputFile/1_1_artist_play_count',na_rep='null')

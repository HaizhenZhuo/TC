#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/4/22 下午7:49
# @Author  : ZHZ
# @Description  : 我们这里的特征有两个,x1是歌曲id,我们只用十个,x2是时间,从1-183天,y是结果

from model.GBDT import *
matrix_date = pd.read_csv("../Data/OutputFile/1_playcount.csv")
x1_x2_y_data = []
date_columns = range(1,184)
song_num = 10
song_count = 1

#我们重新定义column,之前的时间转换太麻烦了我就直接用数字代替
matrix_date.columns =['song_id']+date_columns
for i,j in matrix_date.groupby([matrix_date['song_id']]):
    for k in range(1,184):
        temp = {}
        temp['song_id'] = i
        temp['date'] = k
        temp['count'] = j[k].sum()
        x1_x2_y_data.append(temp)
    song_count = song_count+1
    if song_count>song_num:
        break

#生成我们需要的数据矩阵,这里x_y代表特征和结果放在一起,实际预测的时候要分开
x_y = pd.DataFrame(x1_x2_y_data, columns=['song_id', 'date', 'count'])
#得到GBDT模型
clf = GBDT(x_y[['song_id','date']],x_y['count'])


#生成待预测数据
x_predict_data = []
for i in range(183,240):
    temp={}
    temp['song_id'] = i%10
    temp['date'] = i
    x_predict_data.append(temp)
x_predict = pd.DataFrame(x_predict_data,columns=['song_id','date'])


print "***********************这是我们的第183天到240天的预测结果,error不用管***********************"
print clf.predict(x_predict)
#print matrix_date.song_id.value_counts().size
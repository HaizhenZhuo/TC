#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/4/15 下午2:51
# @Author  : ZHZ


file1 = open("/Users/zhuohaizhen/Downloads/5189-51894/NewNewTopicWordList4.txt","r")
file2 = open("/Users/zhuohaizhen/Downloads/5189-51895/NewNewTopicWordList5.txt","r")

list1 = {}
list2 = {}

for line in file1:
    list1[line.strip().split("##")[0]]=line.strip().split("##")[0]

for line in file2:
    list2[line.strip().split("##")[0]]=line.strip().split("##")[0]


for i in range(0,len(list1)):
    if (list1.get(i)==list2.get(i)):
        print i

print str(len(list1))+"******"
print str(len(list2))+"******"

#list2["好"] = "'"
if list1==list2:
    print "equals"
else:
    print "not equals"
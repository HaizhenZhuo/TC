#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/4/22 下午7:44
# @Author  : ZHZ
# @Description  : 我们这里考虑对10000首歌分别训练一次,特征是date时间
# @知识点  :

from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation
from sklearn.metrics import classification_report

def RF(X,Y):
    #本次变量选取太多,需要跑一段时间,如果想要运行简略版可以考虑使用前10个变量ß
    (data, target) = (X, Y)
    X_tr, X_tt, y_tr, y_tt = cross_validation.train_test_split(data, target, test_size = 0.3, random_state = 0)

    print '----------RandomForest----------'
    clf = RandomForestClassifier(n_estimators = 100, bootstrap = True, oob_score = True)
    clf.fit(X_tr, y_tr)
    print 'OOB Score = %.4f' % clf.oob_score_
    print 'Feature Importance = %s' % clf.feature_importances_
    y_true, y_pred = y_tt, clf.predict(X_tt)
    print(classification_report(y_true, y_pred))

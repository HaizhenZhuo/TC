#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/4/22 下午7:53
# @Author  : ZHZ

from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn import cross_validation
from sklearn.metrics import classification_report
import pandas as pd
import numpy as np
import pylab as pl



def GBDT(X,Y):
    #本次变量选取太多,需要跑一段时间,如果想要运行简略版可以考虑使用前10个变量ß
    #X = X[0:10]
    #Y=Y[0:10]
    #Y = column_or_1d(Y, warn=True)
    # (data, target) = (iris.data, iris.target)
    (data, target) = (X, Y)
    X_tr, X_tt, y_tr, y_tt = cross_validation.train_test_split(data, target, test_size = 0.3, random_state = 0)
    #print X_tr
    '''
    print '----------RandomForest----------'
    clf = RandomForestClassifier(n_estimators = 100, bootstrap = True, oob_score = True)
    clf.fit(X_tr, y_tr)
    print 'OOB Score = %.4f' % clf.oob_score_
    print 'Feature Importance = %s' % clf.feature_importances_
    y_true, y_pred = y_tt, clf.predict(X_tt)
    print(classification_report(y_true, y_pred))
    '''
    print '----------GradientBoosting最终结果的混淆矩阵----------'
    clf = GradientBoostingClassifier(n_estimators = 100, learning_rate = 0.6, random_state = 0)
    clf.fit(X_tr, y_tr)
    print 'Feature Importance = %s' % clf.feature_importances_
    y_true, y_pred = y_tt, clf.predict(X_tt)
    print(classification_report(y_true, y_pred))
    return clf

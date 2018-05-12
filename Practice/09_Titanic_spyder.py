# -*- coding: utf-8 -*-
"""
Created on Sat May 12 21:39:17 2018

@author: 212560227
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

titanic = pd.read_csv("09_Titanic_dataset/titanic_dataset.csv") # 훈련 set
answer = pd.read_csv("09_Titanic_dataset/titanic_answer.csv") # 결과 set (for evaluation)

titanic.head(10)

titanic['age'] = titanic['age'].fillna(titanic['age'].mean())
# sex : male은 0, female은 1로 변환
titanic.loc[titanic['sex']=='male', 'sex'] = 0
titanic.loc[titanic['sex']=='female', 'sex'] = 1
# embark : 2개의 결측값은 최빈값으로 대체하고, one hot encoding 적용
embarked_mode = titanic['embarked'].value_counts().index[0] # 가장 많이 나온 값 (value_counts().index[0])
titanic['embarked'] = titanic['embarked'].fillna(embarked_mode) #embarked 의 NaN 을 가장 많이 나온 값으로 대체 (mode)


df_one_hot_encoded = pd.get_dummies(titanic.embarked)

titanic = pd.concat([titanic, df_one_hot_encoded], axis=1)


def valid_features(col_name):
    g = sns.FacetGrid(titanic, col='survived')
    g.map(plt.hist, col_name, bins=20)

    titanic_survived = titanic[titanic['survived']==1]
    titanic_survived_static = np.array(titanic_survived[col_name])
    print("data length is", '%.2f' % len(titanic_survived_static))
    print("data mean is", '%.2f' % np.mean(titanic_survived_static))
    print("data variance is", '%.2f' % np.var(titanic_survived_static))
    print("data std is", '%.2f' % np.std(titanic_survived_static))
    print("data max is", '%.2f' % np.max(titanic_survived_static))
    print("data min is", '%.2f' % np.min(titanic_survived_static))
    print("data median is", '%.2f' % np.median(titanic_survived_static))
    print("-----------------------")

    titanic_n_survived = titanic[titanic['survived']==0]
    titanic_n_survived_static = np.array(titanic_n_survived[col_name])
    print("data length is", '%.2f' % len(titanic_n_survived_static))
    print("data mean is", '%.2f' % np.mean(titanic_n_survived_static))
    print("data variance is", '%.2f' % np.var(titanic_n_survived_static))
    print("data std is", '%.2f' % np.std(titanic_n_survived_static))
    print("data max is", '%.2f' % np.max(titanic_n_survived_static))
    print("data min is", '%.2f' % np.min(titanic_n_survived_static))
    print("data median is", '%.2f' % np.median(titanic_n_survived_static))
    print("-----------------------")

    tTestResult = stats.ttest_ind(titanic_survived[col_name], titanic_n_survived[col_name])
    tTestResultDiffVar = stats.ttest_ind(titanic_survived[col_name], titanic_n_survived[col_name], equal_var=False)

    print("The t-statistic and p-value assuming equal variances is %.3f and %.3f." % tTestResult)
    print("The t-statistic and p-value not assuming equal variances is %.3f and %.3f" % tTestResultDiffVar)
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

#함수를 사용하지 않고 해보기 

#Survive 한 사람들 list 
titanic_survived = titanic[titanic['survived']==1]
#Survive List 에서 age만 array 로 변경 
titanic_survived_static = np.array(titanic_survived['age'])

#Not Survive List 
titanic_n_survived = titanic[titanic['survived']==0]
#Not Survive List 에서 age만 array 로 변경 
titanic_n_survived_static = np.array(titanic_n_survived['age'])
#숫자 값 외에 name 으로 하면 error 발생 

from scipy import stats
tTestResult = stats.ttest_ind(titanic_survived['age'], titanic_n_survived['age'])

tTestResultTrue= stats.ttest_ind(titanic_survived['age'], titanic_n_survived['age'],equal_var=True)
tTestResultDiffVar = stats.ttest_ind(titanic_survived['age'], titanic_n_survived['age'], equal_var=False)

print (tTestResult)
print (tTestResultTrue)
print (tTestResultDiffVar)

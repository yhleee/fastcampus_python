# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 11:27:41 2018

@author: 212560227
"""

import pandas as pd
import matplotlib.pyplot as plt #시각화 라이브러리
import numpy as np
from sklearn import datasets, linear_model 
from sklearn.metrics import mean_squared_error, r2_score

# 집 값을 예측하는 모델 만들기 
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data', 
                 header=None, sep='\s+')

df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 
              'NOX', 'RM', 'AGE', 'DIS', 'RAD', 
              'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
df.head()

X = df[['RM']].values #아무 컬럼이나 정했다
X.shape
y = df['MEDV'].values #MEDV 가 집값
y.shape

# 훈련 데이터와 테스트 데이터로 나누기
from sklearn.model_selection import train_test_split

#전체 데이터사이즈에서 테스트로 쓰이는 데이터가 30퍼센터
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# 훈련데이터로 학습시키기
regr = linear_model.LinearRegression()
regr.fit(X_train, y_train) #학습이 완료됨

# 테스트 데이터로 결과값 예측
y_pred = regr.predict(X_test)

# 회귀 계수 출력
print('Coefficients: \n', regr.coef_)

# MSE 출력 
print("Mean squared error: %.2f"% mean_squared_error(y_test, y_pred))

# r-score 출력 수정결정계수 0-1 숫자로 나타나는데 1에 가까울수록 예측이 잘된것
print('Variance score: %.2f' % r2_score(y_test, y_pred))

# Plot outputs
plt.scatter(X_test, y_test,  color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show()

###################################################
###################################################
# 다항 회귀모델 학습하기
X = df.iloc[:, :-1].values #마지막 컬럼 빼고 모두 가져온다. 하나의 칼럼만 가져와서 분석했을때보다 값이 더 잘 예측되었음 
y = df['MEDV'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

mlr = linear_model.LinearRegression()
mlr.fit(X_train, y_train)
y_pred = mlr.predict(X_test)

print('Coefficients: \n', mlr.coef_)
print("Mean squared error: %.2f"% mean_squared_error(y_test, y_pred))
print('Variance score: %.2f' % r2_score(y_test, y_pred))


# 데이터 스케일링 : 표준화 (결과는 동일, linear_model 안에 자체구현 되어있기 때문)
from sklearn.preprocessing import StandardScaler
y = df[['MEDV']].values

sc_x = StandardScaler()
X_std = sc_x.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_std, y, test_size=0.3, random_state=0)

mlr = linear_model.LinearRegression()
mlr.fit(X_train, y_train)
y_pred = mlr.predict(X_test)

print('Coefficients: \n', mlr.coef_) #지금은 하나만 보여줘서 값이 똑같이 나옴. 원래 다르게 나와야함 
print("Mean squared error: %.2f"% mean_squared_error(y_test, y_pred))
print('Variance score: %.2f' % r2_score(y_test, y_pred))